from flask_restx import Api
from main.api_resources.api_namespaces import api_v1

api = Api(
        catch_all_404s=True,
        version='2.0',
        title='GitHub Integration',
        prefix='/api',
        description='A simple integration with GitHub',
        doc='/docs'
        )

api.add_namespace(api_v1, path="/v1")