from dracobot2.config import SQL_ENGINE
from dracobot2.models import *

def createDatabase():
    print("Creating Database")
    Base.metadata.create_all(SQL_ENGINE)
    print("Database created")
