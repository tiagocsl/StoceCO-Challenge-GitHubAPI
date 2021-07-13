from flask.globals import request
import requests as req
import json
from github import Github
from src.resources.utils import Sorters
from src.server.instances import r_instance

client_id = '215d69f063d510243a71'
client_secret = '4d0a1a1a21f72007a5e80d7034d9cd04b24f2c5f'
redirect_uri = 'http://localhost:5000/api/authenticate/callback'

r = r_instance.redis_connection()
g = Github(r.get('access_token'))

def authenticate_oauth():
    auth = "https://github.com/login/oauth/authorize?client_id={}&redirect_uri={}&scope=repo user"
    return auth.format(client_id, redirect_uri)


def authenticate_oauth_callback(code):
    data = {"client_id": client_id, 
            "client_secret": client_secret, 
            "code": code}
    request = req.post('https://github.com/login/oauth/access_token', 
                        data, headers={"Accept": 'application/json'}).json()
    access_token = request['access_token']
    r.set('access_token', access_token, 7200)
    print(r.get('access_token'))
    return "Sucessfuly atatch token!"


def most_popular_repo(user):
    user_in_cache = r.get('user')
    user_data = {}
    repositories = []
    if user_in_cache == None or user_in_cache != user:
        # Define o nome do usuário no cache
        # com expiração de 2 segundos
        r.set('user', user, 2, nx=True)        
        try:
            user_data = g.get_user(user)
        except:
            return "An error ocurred in your request!"
        for repo in user_data.get_repos():
            repo_info = {
                        "id": repo.id, 
                        "name": repo.name, 
                        "full_name": repo.full_name, 
                        "stargazers_count": repo.stargazers_count, 
                        "watchers_count": repo.watchers_count, 
                        "forks_count": repo.forks_count, 
                        "open_issues_count": repo.open_issues_count, 
                        "language": repo.language
                        }
            repositories.append(repo_info)
        repositories.sort(key=Sorters.sort_by_stars, reverse=True)
        popular_repository = repositories[0]
        r.set('popular_repo', json.dumps(popular_repository), 2, nx=True)
        return popular_repository    
    else:
        # user_in_cache já existia 
        # e consequentemente o repositorio também
        repo_in_cache = json.loads(r.get('popular_repo'))
        return repo_in_cache


def most_popular_issue(user, repo):
    repo_in_cache = r.get('repo_name_of_issue')
    full_name_of_repo = user + '/' + repo
    issues = []
    if repo_in_cache == None or repo_in_cache != repo:
        # Define o nome do repositório no cache
        # com expiração de 2 segundos
        r.set('repo_name_of_issue', repo, 2, nx=True)
        try:
            repo_data = g.get_repo(full_name_of_repo)
        except:
            return "An error ocurred in your request!"
        popular_issues = repo_data.get_issues(state='open', 
                                            sort='comments')
        for issue in popular_issues:
            issue_with_info = {"id": issue.id, 
                                "number": issue.number,
                                "title": issue.title,
                                "user":{
                                    "login": issue.user.login,
                                    "user_id": issue.user.id,
                                    "user_url": issue.user.url
                                },
                                "state": issue.state,
                                "comments": issue.comments}
            issues.append(issue_with_info)
        r.set('most_commented_issue', json.dumps(issues[0]), 2, nx=True) 
        return issues[0]
    else:
        # nome completo do repositório já existia no cache
        # e consequentemente a issue também
        issue_in_cache = json.loads(r.get('most_commented_issue'))
        return issue_in_cache


def uninteracted_pull(user, repo):
    repo_in_cache = r.get('repo_name_of_pr')
    full_name_of_repo = user + '/' + repo
    uninteracted_prs = []
    if repo_in_cache == None or repo_in_cache != repo:
        # Define o nome do repositório no cache
        # com expiração de 2 segundos
        r.set('repo_name_of_issue', full_name_of_repo, 2, nx=True)
        try:
            repo_data = g.get_repo(full_name_of_repo)
        except:
            return "An error ocurred in your request!"
        pulls = repo_data.get_pulls(state='open',
                                    sort='comments',
                                    direction='desc')
        for pull in pulls:
            parsed_pulls = {"id": pull.id,
                            "number": pull.number,
                            "title": pull.title,
                            "merged_status": pull.merged,
                            "user":{ 
                                "id": pull.user.id,
                                "login": pull.user.login,
                                "name": pull.user.name,
                                "url": pull.user.url
                                },
                            "comments_count": pull.comments}
            uninteracted_prs.append(parsed_pulls)
        r.set('uninteracted_prs', json.dumps(uninteracted_prs), 2, nx=True) 
        return uninteracted_prs
    else:
        # nome completo do repositório já existia no cache
        # e consequentemente o pr também
        uninteracted_pr_in_cache = json.loads(r.get('uninteracted_prs'))
        return uninteracted_pr_in_cache


def create_gitignore(user, repo):
    full_name_of_repo = user + '/' + repo
    try:
        repo_data = g.get_repo(full_name_of_repo)
    except:
        return "An error ocurred in your request!"
    predominant_language = repo_data.language
    try:
        template_gitignore = g.get_gitignore_template(predominant_language)
        repo_data.create_file(path = ".gitignore", 
                                message = "creating gitignore", 
                                content = template_gitignore.source,
                                author=user,
                                branch="main",
                                committer=user
                                )        
    except:
        try:
            contents = repo_data.get_contents(".gitignore")
            repo_data.update_file(contents.path,
                                    message="updating gitignore",
                                    content=template_gitignore.source,
                                    sha=contents.sha,
                                    )
        except:
            return "An error ocurred in your request!"
    
    return "File creating or updating with success!"

def overwriting_a_comment(fst_user, fst_repo, fst_pr_number, 
                            fst_comment_id, snd_user, snd_repo, 
                            snd_pr_number):
    # Chamarei o repositorio que terá seu comentario copiado e deletado
    # de fst_, fst = first. O outro terá snd_, snd = second
    
    # Nome completo do fst_repo
    full_name_of_fst_repo = fst_user + '/' + fst_repo
    # Nome completo do snd_repo
    full_name_of_snd_repo = snd_user + '/' + snd_repo
    try:
        # Dados do fst_repo
        fst_repo_data = g.get_repo(full_name_of_fst_repo)
        # Dados do snd_repo
        snd_repo_data = g.get_repo(full_name_of_snd_repo)
    except:
        return "An error ocurred in your request!"

    # Dados do fst_pull
    fst_pull = fst_repo_data.get_pull(fst_pr_number)
    # Comment do fst_pull
    fst_comment = fst_pull.get_issue_comment(fst_comment_id)

    # Dados do snd_pull
    snd_pull = snd_repo_data.get_pull(snd_pr_number)
    # Criando o comentario no snd_pull, copiando o fst_comment
    snd_pull.create_issue_comment(fst_comment.body)
    # Deletanto o comentario do fst_pull
    fst_comment.delete()

    return "Successfuly create comment!"
    