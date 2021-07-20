import logging
import os
from flask import Flask
from main.config import settings
from main.api import api


# Flask App Initialization
app = Flask(__name__)
app.config.from_object(settings[os.environ.get('APPLICATION_ENV', 'default')])

# Logs Initialization
console = logging.getLogger('console')

# Flask API Initialization
from main.controllers.common_routes import *
from main.controllers.github_authentication import *
from main.controllers.github_integration import *
api.init_app(app)