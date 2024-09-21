import sqlite3

class Field:
    def __init__(self, field_type, **kwargs):
        self.field_type = field_type
        self.kwargs = kwargs

class CharField(Field):
    def __init__(self, max_length=255, **kwargs):
        super().__init__('TEXT', max_length=max_length, **kwargs)

class IntegerField(Field):
    def __init__(self, **kwargs):
        super().__init__('INTEGER', **kwargs)

class Model:
    @classmethod
    def create_table(cls, cursor):
        fields = []
        for name, value in cls.__dict__.items():
            if isinstance(value, Field):
                fields.append(f"{name} {value.field_type}")
        query = f"CREATE TABLE IF NOT EXISTS {cls.__name__} (id INTEGER PRIMARY KEY AUTOINCREMENT, {', '.join(fields)})"
        cursor.execute(query)

    @classmethod
    def get_all(cls):
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {cls.__name__}")
        rows = cursor.fetchall()
        conn.close()
        return [cls(**dict(zip([f.name for f in cls.__dict__.values() if isinstance(f, Field)], row[1:]))) for row in rows]

    @classmethod
    def filter(cls, **kwargs):
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        conditions = ' AND '.join([f"{k} = ?" for k in kwargs.keys()])
        query = f"SELECT * FROM {cls.__name__} WHERE {conditions}"
        cursor.execute(query, list(kwargs.values()))
        rows = cursor.fetchall()
        conn.close()
        return [cls(**dict(zip([f.name for f in cls.__dict__.values() if isinstance(f, Field)], row[1:]))) for row in rows]

    def __init__(self, **kwargs):
        for name, value in kwargs.items():
            setattr(self, name, value)

    def save(self):
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        fields = []
        values = []
        for name, value in self.__class__.__dict__.items():
            if isinstance(value, Field):
                fields.append(name)
                values.append(getattr(self, name))
        query = f"INSERT INTO {self.__class__.__name__} ({', '.join(fields)}) VALUES ({', '.join(['?' for _ in fields])})"
        cursor.execute(query, values)
        conn.commit()
        conn.close()
