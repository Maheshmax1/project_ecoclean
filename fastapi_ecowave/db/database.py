from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from core.config import DB_HOSTNAME, DB_PASSWORD, DB_PORT, DB_USERNAME, DATABASE


# DB_USERNAME = "postgres"
# DB_PASSWORD = "AcademyRootPassword"
# DB_HOSTNAME = "localhost"
# DB_PORT = "5432"
# DATABASE = "eco_website"

DB_URL = f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOSTNAME}:{DB_PORT}/{DATABASE}"

engine = create_engine(DB_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
