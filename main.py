from fastapi import FastAPI

import multiprocessing
from playsound import playsound

app = FastAPI()

class Audio():

    def __init__(self):
        self.p = multiprocessing.Process(target=playsound, args=('./alarm.wav',))
        self.status = False

    def play_audio(self):
        self.p = multiprocessing.Process(target=playsound, args=('./alarm.wav',))
        self.p.start()
        self.status = True

    def stop_audio(self):
        self.p.terminate()
        self.p.join()
        self.status = False

audio = Audio()

stored_password = "monmdp"

@app.post("/alarme/{status}")
async def add_device(status: int):
    if status:
        audio.play_audio()
    return {True}

@app.get("/alarmestop/{password}")
async def stop_alarme(password: str):
    if password == stored_password:
        audio.stop_audio()
        return True
    else:
        return False

@app.get("/alarmestatus")
async def get_alarm():
    return audio.status