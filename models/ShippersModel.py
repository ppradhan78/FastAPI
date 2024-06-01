from typing import Optional
from pydantic import BaseModel
class ShippersModel(BaseModel):
    ShipperID:int
    CompanyName:str
    Phone:str
    Avatar: Optional[str] = None 
    # def __init__(self, ShipperID,CompanyName, Phone,Avatar):
    #     self.ShipperID = ShipperID
    #     self.CompanyName = CompanyName
    #     self.Phone = Phone
    #     self.Avatar = Avatar
    
    