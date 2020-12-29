class Device:

    def __init__(self, device_id):

        self.device_id = device_id
        self.is_registered = False

    def get_device_id(self):
        return self.device_id

    def is_registered(self):
        return self.is_registered