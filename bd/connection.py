from peewee import *
from bd.config import db_name, user, password, host

dbhandle = PostgresqlDatabase(
    db_name,
    user=user,
    password=password,
    host=host
)