from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
    return { 'alarme': True }

@app.post("/alarme/{status}")
async def add_device(name: str, type: str, sensity: int):