class Device(object):
    """docstring for Device."""
    def __init__(self, mac, ip, label='Elektron', data=[]):
        super(Device, self).__init__()
        self.mac = mac
        self.ip = ip
        self.data = data

    def set_mac(self, mac):
        self.mac = mac

    def get_mac(self):
        return self.mac

    def set_ip(self, ip):
        self.ip = ip

    def get_ip(self):
        return self.ip

    def set_label(self, label):
        self.label = label

    def get_label(self):
        return self.label

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data
