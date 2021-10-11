import json

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database.ramdb import RAMDB
from database.repository import RAMRepository, SQLRepository
from database import models

with open('./configs/config.json', 'r') as f:
    db_config_path = json.load(f).get('db_config')

with open(db_config_path, 'r') as f:
    conf = json.load(f)

db = None
repo = None
db_type = conf.get('type')

if db_type == 'RAM':
    db = RAMDB()
    repo = RAMRepository(db)

elif db_type == "PSQL":
    engine = create_engine(conf.get('URL'))
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    models.Base.metadata.create_all(bind=engine)
    repo = SQLRepository(SessionLocal)
