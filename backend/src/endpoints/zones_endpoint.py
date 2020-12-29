from flask import Blueprint, request

from backend.src.api.api_response import APIResponse
from backend.src.api.api_response_error import APIError
from backend.src.zones.zones import Zones


def construct_blueprint(api_manager):

    bp = Blueprint("zones", __name__)

    @bp.route('/', methods=['GET'])
    def get_zones():

        api_key = request.values['api_key']
        if not api_manager.is_key_valid(api_key):
            error = APIError(401, "Invalid API Key")
            return error.get_response()

        return APIResponse(Zones()).get_response()

    return bp
