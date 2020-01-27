from views.base import Api, Response
from models.models import NlpGettingStarted
from flask import request, make_response


class NlpGettingStartedApi(Api, Response):
    def options(self):
        response = make_response()
        response.headers.add("Access-Control-Allow-Origin", "*")
        response.headers.add("Access-Control-Allow-Headers", "*")
        response.headers.add("Access-Control-Allow-Methods", "*")
        return response

    def post(self):
        NlpGettingStarted.validate_body()
        data = request.get_json()
        print('->', data)
        response = NlpGettingStarted.make_prediction(data)
        return self.status_ok(response)
