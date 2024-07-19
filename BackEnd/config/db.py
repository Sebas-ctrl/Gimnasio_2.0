from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:1234@localhost:3306/test"
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://avnadmin:AVNS_ZkZYSnnl4b-9M1oa0gH@mysql-36b8f2d9-estudiante.l.aivencloud.com:24274/bd_gimnasio"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()