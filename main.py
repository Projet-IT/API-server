import json

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder

from database import Database

app = FastAPI()
db = Database()

@app.get('/')
async def root():
    return { 'alarme': True }

@app.get("/getdevices")
async def getdevices():
    devices = jsonable_encoder(db.get_devices())
    return devices


@app.get("/getconfig/{id}")
async def getconfig(id: int):

    config = jsonable_encoder(db.get_device_config(id))

    return config

@app.post("/post/adddevice/{name}/{type}/{sensity}")
async def add_device(name: str, type: str, sensity: int):
    try:
        db.add_device(name, type, sensity)
        return {True}
    except Exception as e:
        print(e)
        return {False}