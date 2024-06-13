from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import app.schemas as schemas
import app.crud as crud
from app.db import get_db

router = APIRouter(prefix="/configurations", tags=["configurations"])

@router.post("/", response_model=schemas.ConfigurationDB)
def create_configuration(configuration: schemas.ConfigurationCreate, db: Session = Depends(get_db)):
    """This is an api endpoint for creating new country configuration which accepts the data from user in json format

    Args:
        configuration (schemas.ConfigurationCreate): all necessary details of country as json object

    Raises:
        HTTPException: if given country code already exist in the database

    Returns:
        json: return created country configuation as json object
    """
    db_configuration = crud.get_configuration(db, country_code=configuration.country_code)
    if db_configuration:
        raise HTTPException(status_code=400, detail="Configuration already exists")
    return crud.create_configuration(db=db, configuration=configuration)



@router.get("/{country_code}", response_model=schemas.ConfigurationDB)
def read_configuration(country_code: str, db: Session = Depends(get_db)):
    """This is an api endpoint to get the country configuration corresponding to country code

    Args:
        country_code (str): country code in upper case international standard country code 

    Raises:
        HTTPException: if country code is not present in database

    Returns:
        json: country configuration as an json object
    """
    db_configuration = crud.get_configuration(db, country_code=country_code)
    if db_configuration is None:
        raise HTTPException(status_code=404, detail="Configuration not found")
    
    return db_configuration


# api endpoint for update configuration
@router.put("/", response_model=schemas.ConfigurationDB)
def update_configuration(configuration: schemas.ConfigurationUpdate, db: Session = Depends(get_db)):
    """This is an api endpoint to update country configuration

    Args:
        configuration (schemas.ConfigurationUpdate): country configuration as json object
       

    Returns:
        json: return updated country configuration in json format
    """
    return crud.update_configuration(db=db, country_code=configuration.country_code, configuration=configuration)

# api endpoint for delete configuration
@router.delete("/{country_code}", response_model=schemas.ConfigurationDB)
def delete_configuration(country_code: str, db: Session = Depends(get_db)):
    """This is an api endpoint for deleting country configuration corresponding to given country code.

    Args:
        country_code (str): Counry code in upper case letter

    Returns:
        json: Return data of deleted country
    """
    return crud.delete_configuration(db=db, country_code=country_code)



