from db.database import Base
from sqlalchemy import Column , Integer , String

class Temp(Base):
    __tablename__ = "temp"

    id =Column(Integer, primary_key = True)
    name= Column(String)
