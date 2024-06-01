# import random
# from fastapi import FastAPI
# from enum import Enum

# app=FastAPI()

# # @app.get("/home")
# @app.get("/home",tags=["FAST API with simple CURD"])
# def welcome():
#     return "Welcome to Fast API" 
# # Path parameters
# @app.get("/users/{userid}",tags=["User details"])
# def users(userid:int):
#     return f"UsersFast API user id {userid}" 

# #Query String
# @app.get("/dept/{userid}",tags=["User details"])
# def users(userid:int):
#     if not userid:
#         return "please enter number"
#     return random.random()