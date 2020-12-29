class Zone:

    def __init__(self, name) -> None:
        super().__init__()
        self.name = name

    def get_name(self):
        return self.name

    def json_rep(self):
        return self.__dict__