from peewee import *
import bd.connection


class BaseModel(Model):
    class Meta:
        database = bd.connection.dbhandle


class Counter(BaseModel):
    id = PrimaryKeyField(null=False)
    ls_id = IntegerField()
    old_indications = CharField(max_length=100)
    new_indications = CharField(max_length=100)
    data_verification = CharField(max_length=100)

    class Meta:
        db_table = "counter"


class NumberLs(BaseModel):
    id = PrimaryKeyField(null=False)
    long_ls = CharField(max_length=13)
    id_user_telegram = CharField(max_length=30)

    class Meta:
        db_table = "number_ls"
