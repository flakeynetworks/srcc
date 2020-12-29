from flask import Blueprint, request

from backend.src.api.api_response import APIResponse
from backend.src.api.api_response_error import APIError


def construct_blueprint(api_manager):

    bp = Blueprint("device", __name__)

    @bp.route('/registration/<device_id>', methods=['POST'])
    def register_device(device_id):

        api_key = request.values['api_key']
        if not api_manager.is_key_valid(api_key):
            error = APIError(401, "Invalid API Key")
            return error.get_response()

        return APIResponse().get_response()

    return bp
