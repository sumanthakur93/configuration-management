from sqlalchemy import Column, Integer, String, JSON
from app.db import Base

class Configuration(Base):
    __tablename__ = "configurations"

    id = Column(Integer, primary_key=True, index=True)
    country_code = Column(String, unique=True, index=True)
    country_name = Column(String)
    requirements = Column(JSON)
