from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

connection_str = 'postgresql://postgres:postgres@db:5432/postgres'
print(connection_str)

engine = create_engine(connection_str)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
# try:
#     with engine.connect() as connection_str:
#         print('Successfully connected to the PostgreSQL database')
# except Exception as ex:
#     print(f'Sorry failed to connect: {ex}')