from flask import request, redirect
from flask_restx import Resource, fields
import src.resources.services as services
from src.server.instances import *

app, api = server.app, server.api
ns = api.namespace("StoneCO-Challenge",
                    description="List of Operations")


@api.route('/home')
class Hello(Resource):
    def get(self,):
        return "Hello my dear friend, welcome to my humble Github integration :)"        


@api.route('/api/authenticate')
class login(Resource):
    def get(self,):
        return redirect(services.authenticate_oauth())


@api.route('/api/authenticate/callback')
class login(Resource):
    def get(self,):
        code = request.args.get('code')
        return services.authenticate_oauth_callback(code)


@api.route('/test-redis')
class testing_redis(Resource):
    def get(self,):
        try:
            return r_instance.redis_connection().ping()
        except Exception as e:
            print(e)


@api.route('/api/repos/<string:user>/popular-repository')
@ns.response(404, "An error ocurred in your request!")
class popular_repository(Resource):
    @ns.response(200, "successfully")
    def get(self, user):
        return services.most_popular_repo(user)


@api.route('/api/repos/<string:user>/<string:repo>/popular-issue')
@ns.response(404, "An error ocurred in your request!")
class popular_issues(Resource):
    @ns.response(200, "successfully")
    def get(self, user, repo):
        return services.most_popular_issue(user, repo)


@api.route('/api/repos/<string:user>/<string:repo>/uninteracted-pull')
@ns.response(404, "An error ocurred in your request!")
class uninteracte_pull_request(Resource):
    @ns.response(200, "successfully")
    def get(self, user, repo):
        return services.uninteracted_pull(user, repo)


@api.route('/api/repos/pull/create-comment')
class comment_copy_delete(Resource):
    def post(self,):
        data = request.json
        fst_user = data['fst_user']
        fst_repo = data['fst_repository']
        fst_pr_number = data['fst_pull_number'] 
        fst_comment_id = data['fst_comment_id']
        snd_user = data['snd_user']
        snd_repo = data['snd_repository']
        snd_pr_number = data['snd_pull_number']
        return services.overwriting_a_comment(fst_user, fst_repo, 
                                                fst_pr_number, fst_comment_id, 
                                                snd_user, snd_repo, snd_pr_number)


@api.route('/api/repos/<string:user>/<string:repo>/create-gitignore')
class create_gitignore(Resource):
    def post(self, user, repo):
        return services.create_gitignore(user, repo)        