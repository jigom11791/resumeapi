import databases
import ormar
import sqlalchemy

from ormar import (
    Integer, 
    String, 
    ForeignKey
)
from typing import Optional

from config import settings

database = databases.Database(settings.db_url)
metadata = sqlalchemy.MetaData()
email_regex = r'^[\w\-\.]+@([\w-]+\.)+[\w-]{2,}$'
phone_regex = r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'

class BaseModel(ormar.MetaData):
    metadata=metadata
    database=database

class Skill(ormar.Model):
    class Meta(BaseModel):
        table_name="skill"
    
    name:str = String(max_length=128, nullable=False)
    proficency:str = String(nullable=False, chioces=[
        'beginner',
        'intermediate',
        'advanced'
    ])


class User(ormar.Model):
    class Meta(BaseModel):
        table_name="user"
    id:int = Integer(primary_key=True)
    name:str = String(max_length=128, nullable=False)
    email:str = String(
        max_length=128, 
        regex=email_regex,
        unique=True, 
        nullable=False)
    phone:str = String(regex=phone_regex)
    github:str = String(max_length=400)
    skills:Optional[Skill] = ForeignKey(Skill)
