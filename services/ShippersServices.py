import pyodbc
import pandas as pd
from models.ShippersModel import ShippersModel


class ShippersServices():
    def __init__(self):
           connStr="Driver=SQL Server;Server=home\\SQLEXPRESS;Database=Northwind;Trusted_Connection=yes;"
           self.conn = pyodbc.connect(connStr)
           self.conn.autocommit=True
           self.cur = self.conn.cursor()

    def GetList(self):
          query='select  * from Shippers'
          df=pd.read_sql(query,self.conn)
          return df
    
    def GetById(self,id):
          query='select  * from Shippers where ShipperID='+id
          df=pd.read_sql(query,self.conn)
          return df
    
    def createShippers(self,ShippersModel):
        query=f"INSERT INTO Shippers(CompanyName,Phone)VALUES('{ShippersModel.CompanyName}','{ShippersModel.Phone}')"
        self.cur.execute(query)
        if self.cur.rowcount>0:
             return {"message":"Shippers information Save Successfully.","statuscode":201};
        else:
             return {"message":"Faill to save Shippers information.","statuscode":202};

    def updateShippers(self,ShippersModel):
        query=f"UPDATE Shippers SET CompanyName='{ShippersModel.CompanyName}' , Phone='{ShippersModel.Phone}' WHERE ShipperID={ShippersModel.ShipperID}"
        self.cur.execute(query)
        if self.cur.rowcount>0:
             return {"message":"Shippers information Updated Successfully.","statuscode":204}
        else:
             return {"message":"Nothing to Update Shippers information.","statuscode":202}
    
    def deleteShippers(self,id):
        self.cur.execute(f"DELETE FROM Shippers WHERE ShipperID={id}")
        if self.cur.rowcount>0:
             return  {"message":"Shippers information Deleted Successfully.","statuscode":201}
        else:
             return {"message":"Nothing Deleted Shippers information.","statuscode":202}    
        
    

 
       