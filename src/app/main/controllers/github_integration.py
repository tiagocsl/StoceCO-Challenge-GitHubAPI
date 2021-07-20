from flask_restx import Resource
from flask import request as req
from main.api_resources.api_namespaces import api_v1
from main.api_resources import api_models
from main.services import github_integration_service as gi_service


@api_v1.route('/repos/popular-repository')
class popular_repository(Resource):
    @api_v1.response(200, 'The most popular open repository.')
    @api_v1.response(404, 'An error ocurred in your request!')
    @api_v1.doc('most_popular_repository')   
    @api_v1.expect(api_models.most_popular_repo, responses=api_models.most_popular_repo_reponse)
    def get(self, user):
        try:
            return gi_service.most_popular_repo(user)
        except Exception as e:
            api_v1.abort(404, e.__doc__, status='An error ocurred in your request!', statusCode=404)


@api_v1.route('/repos/popular-issue')
class popular_issues(Resource):
    @api_v1.response(200, 'The most popular open issue.')
    @api_v1.response(404, 'An error ocurred in your request!')
    @api_v1.doc('most_popular_issue')
    @api_v1.expect(api_models.most_popular_issue, responses=api_models.most_popular_issue_reponse)
    def get(self, user, repo):
        try:
            return gi_service.most_popular_issue(user, repo)
        except Exception as e:
            api_v1.abort(404, e.__doc__, status='An error ocurred in your request!', statusCode=404)


@api_v1.route('/repos/uninteracted-pull')
class uninteracte_pull_request(Resource):
    @api_v1.response(200, 'List of open pull requests that have not changed.')
    @api_v1.response(404, 'An error ocurred in your request!')
    @api_v1.doc('uninteracted_pull_request', responses=api_models.uninteracte_pull_request_reponse)
    @api_v1.expect(api_models.uninteracte_pull_request)
    def get(self, user, repo):
        try:
            return gi_service.uninteracted_pull(user, repo)
        except Exception as e:
            api_v1.abort(404, e.__doc__, status='An error ocurred in your request!', statusCode=404)


@api_v1.route('/repos/pull/create-comment')
class comment_copy_delete(Resource):    
    @api_v1.response(201, 'The original comment has been successfully replicated and deleted!')
    @api_v1.response(404, 'An error ocurred in your request!')
    @api_v1.doc('copy_and_delete_comment', responses=api_models.copy_and_delete_comment_reponse)
    @api_v1.expect(api_models.copy_and_delete_comment)
    def post(self,):
        data = req.json
        fst_fullname_repo = data['fst_fullname_repo']
        fst_pr_number = data['fst_pull_number'] 
        fst_comment_id = data['fst_comment_id']
        snd_fullname_repo = data['snd_fullname_repo']
        snd_pr_number = data['snd_pull_number']
        try:
            return gi_service.overwriting_a_comment(fst_fullname_repo, 
                                                    fst_pr_number, fst_comment_id, 
                                                    snd_fullname_repo, snd_pr_number)
        except Exception as e:
            api_v1.abort(404, e.__doc__, status='An error ocurred in your request!', statusCode=404)


@api_v1.route('/repos/create-gitignore')
class create_gitignore(Resource):
    @api_v1.response(201, 'The GitIgnore file was created or overwritten successfully!')
    @api_v1.response(404, 'An error ocurred in your request!')
    @api_v1.doc('create_or_overwrite_gitignore', responses=api_models.create_or_overwrite_gitignore_reponse)
    @api_v1.expect(api_models.create_or_overwrite_gitignore)
    def post(self,):
        data = req.json
        fullname_repo = data['fullname_repo']
        author = data['author']
        try:
            return gi_service.create_gitignore(fullname_repo, author)       
        except Exception as e:
                api_v1.abort(404, e.__doc__, status='An error ocurred in your request!', statusCode=404)



