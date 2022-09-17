"""
    Acá estamos estableciendo la conexión a la DB.
    El archivo de la DB (store.db) queda en le mismo directorio.
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQL_ALCHEMY_DB_URL = "sqlite:///./store.db"

connect_args = {"check_same_thread": False}

# Creamos el "engine" de SQLAlchemy
engine = create_engine(SQL_ALCHEMY_DB_URL)

# Sesiones de la DB
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Esto nos ayuda mas adelante a crear modelos de la DB o clases (modelos ORM)
Base = declarative_base()