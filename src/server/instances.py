from flask import Flask
from flask_restx import Api
import redis


class Server():
    def __init__(self,):
        self.app = Flask(__name__)
        self.api = Api(self.app,
            version='1.0',
            title='GitHub Integration',
            default='/',
            description='A simple integration with GitHub',
            doc='/api/docs'
        )
    
    def run(self,):
        self.app.run(
            host='localhost',
            port=5000,
            debug=True
        )


class redis_instance():
    def redis_connection(self,):
        r = redis.Redis(
            host='cache',
            port=6379,
            charset='utf-8',
            decode_responses=True
        )
        return r

server = Server()
r_instance = redis_instance()