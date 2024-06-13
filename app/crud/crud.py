from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models import Configuration
import app.schemas as schemas


def get_configuration(db: Session, country_code: str):
    return db.query(Configuration).filter(Configuration.country_code == country_code).first()

def create_configuration(db: Session, configuration: schemas.ConfigurationCreate):
    db_configuration = Configuration(**configuration.model_dump())
    db.add(db_configuration)
    db.commit()
    db.refresh(db_configuration)
    return db_configuration

def update_configuration(db: Session, country_code: str, configuration: schemas.ConfigurationUpdate):
    db_configuration = get_configuration(db, country_code)
    if not db_configuration:
        raise HTTPException(status_code=404, detail="Configuration not found")
    for key, value in configuration.model_dump().items():
        setattr(db_configuration, key, value)
    db.commit()
    db.refresh(db_configuration)
    return db_configuration

def delete_configuration(db: Session, country_code: str):
    """Controller to delete the existing country congiguration 

    Args:
        db (Session): 
        country_code (str): accept country code in upper case international standard

    Raises:
        HTTPException: if data with given country code is not present in this database

    Returns:
        json: return country configuration as json format
    """
    db_configuration = get_configuration(db, country_code)
    if not db_configuration:
        raise HTTPException(status_code=404, detail="Configuration not found")
    db.delete(db_configuration)
    db.commit()
    return db_configuration


