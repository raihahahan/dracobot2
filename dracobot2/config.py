from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
from dracobot2.models import *
import pymysql

load_dotenv()

db_user = os.environ["DB_USERNAME"]
db_password = os.environ["DB_PASSWORD"]
db_host = os.environ["DB_HOST"]
db_name = os.environ["DB_NAME"]
db_port = os.environ["DB_PORT"]

DATABASE_URL = f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

SQL_ENGINE = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=SQL_ENGINE, autocommit=False, autoflush=False)
