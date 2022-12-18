from typing import Optional
from fastapi import Body, FastAPI
from pydantic import BaseModel
from pymongo import MongoClient
from flask import request

# from flask_pymongo import PyMongo
# from flask import Flask
# from termcolor import colored

class Post(BaseModel):
    title : str
    description : str
    # default_val : bool = True
    # rating : Optional[int] = None

app = FastAPI()
client = MongoClient("mongodb://localhost:27017/")
db = client["todo_api"]
collec = db["api_collection"]

@app.get('/')
def root():
    return {"msg": "root index with app.get :)"}

@app.get('/get_method')
def get_request(all_data: Post):
    return {"message": all_data}

@app.post('/post')
def post_request(recieved_data: Post):
    print("\n Pydantic BaseModel :")
    print(recieved_data)
    print("\n Python Dictionary :")
    print(recieved_data.dict())
    data_to_insert = {'title': recieved_data.title, 'description': recieved_data.description}
    try:
        collec.insert_one(data_to_insert)
    except Exception as e:
        print("Error: ", str(e))
    return {"data": recieved_data}