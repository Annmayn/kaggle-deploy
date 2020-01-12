from views.base import Api, Response
from models.models import NlpGettingStarted
from flask import request


class NlpGettingStartedApi(Api, Response):
    def post(self):
        NlpGettingStarted.validate_body()
        response = NlpGettingStarted.make_prediction(request.get_json())
        return self.status_ok(response)
