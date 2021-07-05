from enum import unique
from models.base_model import BaseModel
import peewee as pw


class User(BaseModel):
    username = pw.CharField(unique=True, null=False)
    email = pw.CharField(unique= True, null= False)
    first_name = pw.CharField(null=False)
    last_name = pw.CharField(null= False)

