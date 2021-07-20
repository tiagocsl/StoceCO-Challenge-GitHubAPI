from flask import request as req
from flask import redirect
from flask_restx import Resource
from main.api_resources.api_namespaces import api_v1
from main.services import github_authentication_service as ga_service


@api_v1.route('/authenticate')
class authenticate(Resource):
    def get(self,):
        return redirect(ga_service.authenticate_oauth())


@api_v1.route('/authenticate/callback')
@api_v1.param('code', _in='query')
class authenticate_callback(Resource):    
    @api_v1.doc('create_access_token')
    def get(self,):        
        code = req.args.get('code')
        return ga_service.authenticate_oauth_callback(code)

   