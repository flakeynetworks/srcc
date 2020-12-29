import json

from flask import Response


class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj,'json_rep'):
            return obj.json_rep()
        else:
            return json.JSONEncoder.default(self, obj)


class APIResponse:

    def __init__(self, data=None):
        self.status = 200
        self.data = data

    def get_response(self):
        return Response(self.to_json(), status=self.status, mimetype='application/json')

    def to_json(self):
        return json.dumps(self.__dict__, cls=ComplexEncoder)