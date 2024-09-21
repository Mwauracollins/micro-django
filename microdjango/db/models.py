class Model:
    def __init__(self, **kwargs):
        for field_name, value in kwargs.items():
            setattr(self, field_name, value)

    @classmethod
    def create_table(cls):
        print(f"Creating table for {cls.__name__}")


class Field:
    def __init__(self, default=None):
        self.default = default


class CharField(Field):
    def __init__(self, max_length=255, **kwargs):
        super().__init__(**kwargs)
        self.max_length = max_length


class IntegerField(Field):
    pass


class ForeignKey(Field):
    def __init__(self, to, on_delete, **kwargs):
        super().__init__(**kwargs)
        self.to = to
        self.on_delete = on_delete
