from http import HTTPStatus
from flask import request, abort, jsonify


class Response:
    def bad_request(self, message):
        abort(HTTPStatus.BAD_REQUEST, message)

    def status_ok(self, message):
        response = jsonify({"result":message})
        response.headers.add('Access-Control-Allow-Origin', 'https://kaggle-ml-web.herokuapp.com')
        return {"result":message}


class Api:
    def dispatch_request(self, *args, **kwargs):
        request_method = request.method.lower()
        print("r: ", request_method)
        meth = getattr(self, request_method, None)
        print("m: ", meth)
        if meth is not None:
            print("Method: ", meth)
            return meth(*args, **kwargs)
        else:
            abort(405, "Method not allowed")

    @classmethod
    def as_view(cls, *class_args, **class_kwargs):
        def view(*args, **kwargs):
            self = cls(*class_args, **class_kwargs)
            return self.dispatch_request(*args, **kwargs)
        return view
