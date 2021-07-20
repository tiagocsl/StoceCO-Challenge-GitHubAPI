from flask_restx import Namespace

# ---------------------- #
# Versionamento de API's #
# ---------------------- #

api_v1 = Namespace("StoneCO-Challenge-v1",
                description="List of Operations of v1"
                )