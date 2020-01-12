from flask import abort
from http import HTTPStatus

class Model:
    base_location = 'static/models/'
    model_name = None
    vectorizer_name = None
    required = []