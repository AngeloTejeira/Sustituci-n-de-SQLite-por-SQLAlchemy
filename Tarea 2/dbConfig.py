from sqlalchemy import create_engine
from sqlalchemy_utils import create_database, database_exists
from modelo import Base

def get_engine(user, password, host, port, dbname):
  url = f'mysql://{user}:{password}@{host}:{port}/{dbname}'
  crearTablas = False
  if not database_exists(url):
    crearTablas = True
    create_database(url)
  engine = create_engine(url, pool_size=50, echo=False)
  
  if crearTablas:
    Base.metadata.create_all(engine)

  return engine