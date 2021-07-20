import os
import requests as req
from main.cache_instance import redis_connection

r = redis_connection()

def authenticate_oauth():
    auth = "https://github.com/login/oauth/authorize?client_id={}&redirect_uri={}&scope=repo user"
    return auth.format(os.environ.get('CLIENT_ID'), os.environ.get('REDIRECT_URI'))


def authenticate_oauth_callback(code):
    data = {"client_id": os.environ.get('CLIENT_ID'), 
            "client_secret": os.environ.get('CLIENT_SECRET'), 
            "code": code}
    request = req.post('https://github.com/login/oauth/access_token', 
                        data, headers={"Accept": 'application/json'}).json()
    access_token = request['access_token']
    r.set('access_token', access_token, 7200)
    print(r.get('access_token'))
    return "Sucessfuly atatch token!"