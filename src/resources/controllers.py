from flask import Flask
from flask_restx import Api, Resource

from src.resources import services

from src.server.instance import server

app, api = server.app, server.api

@api.route('/<string:user>')
class Hello(Resource):
    def get(self, user):
        return "Hello " + user

@api.route('/api/repos/<string:user>/popular-repository')
class popularRepository(Resource):
    def get(self, user):
        return services.mostPopularRepo(user)

@api.route('/api/repos/<string:user>/<string:repo>/popular-issue')
class popularIssues(Resource):
    def get(self, user, repo):
        return services.mostCommentedIssue(user, repo)

@api.route('/api/repos/<string:user>/<string:repo>/uninteracted-pull')
class uninteractePullReq(Resource):
    def get(self, user, repo):
        return services.uninteractedPull(user, repo)