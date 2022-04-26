from peewee import *

db = PostgresqlDatabase('contacts', user='postgres',
                        password='123', host='localhost', port=5432)


class BaseModel(Model):
    class Meta:
        database = db

class People(BaseModel):
    name = CharField()
    phone_number = CharField()
    
