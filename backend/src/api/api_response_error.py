import json

from flask import Response


class APIError:

    def __init__(self, status=400, reason=None):
        self.status = status
        self.reason = reason

    def get_response(self):
        return Response(self.to_json(), status=self.status, mimetype='application/json')

    def to_json(self):
        return json.dumps(self.__dict__)