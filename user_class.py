class User(object):
    """docstring for User."""
    def __init__(self, nombre, password, config, devices=[], tasks=[]):
        super(User, self).__init__()
        self.nombre = nombre
        self.password = password
        self.devices = devices
        self.tasks = tasks
        self.config = config

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_nombre(self):
        return self.nombre

    def set_password(self, password):
        self.password = password

    def get_password(self):
        return self.password

    def set_config(self, config):
        self.config = config

    def get_config(self):
        return self.config

    def set_devices(self, devices):
        self.devices = devices

    def get_devices(self):
        return self.devices

    def set_tasks(self, tasks):
        self.tasks = tasks

    def get_tasks(self):
        return self.tasks
