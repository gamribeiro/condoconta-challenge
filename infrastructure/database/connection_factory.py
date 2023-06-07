from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool
from sqlalchemy.orm import declarative_base
from sqlalchemy_utils import generic_repr

Base = generic_repr(declarative_base())

# from infrastructure.common.config import get_key, ENVIRONMENT

_database_url = "postgresql://{}:{}@{}:{}/{}".format(
    'gamribeiro',
    'postgres',
    'localhost',
    '5432',
    'condoconta_challenge',
)
_engine = create_engine(
    _database_url, poolclass=NullPool, connect_args={"connect_timeout": 5}
)

Session = scoped_session(sessionmaker(bind=_engine))
