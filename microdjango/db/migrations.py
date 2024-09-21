class Migration:
    operations = []

class CreateModel:
    def __init__(self, name, fields):
        self.name = name
        self.fields = fields