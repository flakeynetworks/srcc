from backend.src.api.api_response import APIResponse
from backend.src.zones.zones import Zones


def test_zones_to_json():

    zones = Zones()
    print(zones.to_json())

def test_api_zones_to_json():

    response = APIResponse(Zones().to_json()).get_response()