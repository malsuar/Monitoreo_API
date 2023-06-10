from typing import Optional 
from pydantic import BaseModel
import datetime

class Monitoreo(BaseModel):
    _id         : Optional[str]
    lugar       : str
    autor       : str
    temperatura : float
    humedad     : float
    createdAT   : Optional[datetime.datetime]
    updatedAT   : Optional[datetime.datetime]


