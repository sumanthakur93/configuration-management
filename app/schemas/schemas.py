from pydantic import BaseModel, Field
from typing import Dict, Any

class ConfigurationBase(BaseModel):
    country_code: str = Field(..., example="IN")
    country_name: str = Field(..., example="India")
    requirements: Dict[str, Any] = Field(..., example={"Business Name": "string", "PAN": "string", "GSTIN": "string"})

class ConfigurationCreate(ConfigurationBase):
    pass

class ConfigurationUpdate(ConfigurationBase):
    pass

class ConfigurationDB(ConfigurationBase):
    id: int

    class Config:
        orm_mode = True
