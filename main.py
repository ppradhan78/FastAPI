from typing import Annotated, Union
from fastapi import Body, Cookie, FastAPI, File, Form, HTTPException, Header, Path, Query, UploadFile
from pydantic import BaseModel, Field
import pyodbc
import pandas as pd;
from services.ShippersServices import ShippersServices
from models.ShippersModel import ShippersModel

app=FastAPI()
obj=ShippersServices()

@app.get("/Index",tags=["FAST API with simple CURD"])
async  def welcome():
    return "Welcome to Fast API" 

@app.get("/About",tags=["FAST API with simple CURD"])
async  def welcome():
    return "FastAPI serve as frameworks for building web APIs in Python." 

@app.get("/Contactus",tags=["FAST API with simple CURD"])
async  def welcome():
    return "https://fastapi.tiangolo.com/tutorial/" 

@app.get("/",tags=["FAST API with simple CURD"])
async  def welcome():
    return "Welcome to Fast API" 

@app.get("/List",tags=["Get Shippers List"])
def GetShippersList():
    df=obj.GetList()
    return df.to_dict('records')

@app.get("/GetById",tags=["Get Shippers details by Id"])
def GetById(id):
    df=obj.GetById(id)
    return df.to_dict('records')

@app.post("/Create", tags=["Create Shippers"])
def Create(shippers: ShippersModel):
    result=obj.createShippers(shippers)
    return result

@app.put("/Update", tags=["Update Shippers"])
def Update(shippers: ShippersModel):
    result=obj.updateShippers(shippers)
    return result


@app.delete("/Delete",tags=["Delete Shippers By Id"])
def Delete(id):
    result=obj.deleteShippers(id)
    return result

@app.get("/items/")
async def read_items(q: Annotated[str, Query(min_length=3)]):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

@app.get("/NumValidation/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(title="The ID of the item to get")],
    q: Annotated[Union[str, None], Query(alias="item-query")] = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    
@app.put("/Range/{item_id}")
async def update_item(
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
    q: Union[str, None] = None,
    item: Union[Item, None] = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    return results



class Item(BaseModel):
    name: str
    description: str | None = Field(
        default=None, title="The description of the item", max_length=3
    )
    price: float = Field(gt=0, description="The price must be greater than zero")
    tax: float | None = None


@app.put("/maxlength/{item_id}")
async def update_item(item_id: int, item: Annotated[Item, Body(embed=True)]):
    results = {"item_id": item_id, "item": item}
    return results

# @app.get("/Cookies/")
# async def read_items(ads_id: Annotated[str | None, Cookie()] = None):
#     return {"ads_id": ads_id}
 



@app.get("/header/")
async def read_items(x_token: Annotated[list[str] | None, Header()] = None):
    return {"X-Token values": x_token}

@app.post("/statuscode/", status_code=201)
async def create_item(name: str):
    return {"name": name}
# Define Form parameters
@app.post("/login/")
async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    return {"username": username}

# File upload

@app.post("/files/")
async def create_file(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}

# Handling Errors

@app.get("/items/{item_id}")
async def read_item(item_id: str):
    if item_id not in Item:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item": Item[item_id]}