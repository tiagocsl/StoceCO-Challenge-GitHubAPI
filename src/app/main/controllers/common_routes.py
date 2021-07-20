from flask_restx import Resource
from main.api_resources.api_namespaces import api_v1
from main.cache_instance import redis_connection

r = redis_connection()

@api_v1.route('/home')
class Hello(Resource):
    def get(self,):
        return "Hello my dear friend, welcome to my humble Github integration :)"        


@api_v1.route('/test-redis')
class testing_redis(Resource):
    @api_v1.doc('test_redis_connection')
    def get(self,):
        try:
            return r.ping()
        except Exception as e:
            print(e)