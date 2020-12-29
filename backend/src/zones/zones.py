from backend.src.zones.zone import Zone


class Zones:

    def __init__(self) -> None:
        super().__init__()
        self.zones = [Zone("room"), Zone("rack")]

    def json_rep(self):
        return self.zones