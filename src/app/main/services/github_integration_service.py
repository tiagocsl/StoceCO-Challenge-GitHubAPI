import json
from github import Github
from main.utils.utilitaries import Sorters
from main.cache_instance import redis_connection

r = redis_connection()
g = Github(r.get('access_token'))

def most_popular_repo(user):
    user_in_cache = r.get('user')
    user_data = {}
    repositories = []
    if user_in_cache == None or user_in_cache != user:
        # Define o nome do usuário no cache
        # com expiração de 30 segundos
        r.set('user', user, 30, nx=True) 
        user_data = g.get_user(user)
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
        r.set('popular_repo', json.dumps(popular_repository), 30, nx=True)
        return popular_repository    
    else:
        # user_in_cache já existia 
        # e consequentemente o repositorio também
        repo_in_cache = json.loads(r.get('popular_repo'))
        return repo_in_cache


def most_popular_issue(fullname_repo):
    repo_in_cache = r.get('repo_name_of_issue')
    issues = []
    if repo_in_cache == None or repo_in_cache != fullname_repo:
        # Define o nome do repositório no cache
        # com expiração de 30 segundos
        r.set('repo_name_of_issue', fullname_repo, 30, nx=True)
        repo_data = g.get_repo(fullname_repo)
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
        r.set('most_commented_issue', json.dumps(issues[0]), 30, nx=True) 
        return issues[0]
    else:
        # nome completo do repositório já existia no cache
        # e consequentemente a issue também
        issue_in_cache = json.loads(r.get('most_commented_issue'))
        return issue_in_cache


def uninteracted_pull(fullname_repo):
    repo_in_cache = r.get('repo_name_of_pr')
    uninteracted_prs = []
    if repo_in_cache == None or repo_in_cache != fullname_repo:
        # Define o nome do repositório no cache
        # com expiração de 30 segundos
        r.set('repo_name_of_issue', fullname_repo, 30, nx=True)
        repo_data = g.get_repo(fullname_repo)
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
        r.set('uninteracted_prs', json.dumps(uninteracted_prs), 30, nx=True) 
        return uninteracted_prs
    else:
        # nome completo do repositório já existia no cache
        # e consequentemente o pr também
        uninteracted_pr_in_cache = json.loads(r.get('uninteracted_prs'))
        return uninteracted_pr_in_cache


def create_gitignore(fullname_repo, author):
    repo_data = g.get_repo(fullname_repo)
    predominant_language = repo_data.language
    try:
        template_gitignore = g.get_gitignore_template(predominant_language)
        repo_data.create_file(path = ".gitignore", 
                                message = "creating gitignore", 
                                content = template_gitignore.source,
                                author=author,
                                branch="main",
                                committer=author
                                )        
    except:
        contents = repo_data.get_contents(".gitignore")
        repo_data.update_file(contents.path,
                              message="updating gitignore",
                              content=template_gitignore.source,
                              sha=contents.sha)
    
    return "File creating or updating with success!"

def overwriting_a_comment(fst_fullname_repo, fst_pr_number, fst_comment_id,
                            snd_fullname_repo, snd_pr_number):
    # Chamarei o repositorio que terá seu comentario copiado e deletado
    # de fst_, fst = first. O outro terá snd_, snd = second

    # Dados do fst_repo
    fst_repo_data = g.get_repo(fst_fullname_repo)
    # Dados do snd_repo
    snd_repo_data = g.get_repo(snd_fullname_repo)

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
    