from fastapi import FastAPI

import multiprocessing
from playsound import playsound

app = FastAPI()

class Audio():

    def __init__(self):
        self.p = multiprocessing.Process(target=playsound, args=('./alarm.wav',))

    def play_audio(self):
        self.p.start()

    def stop_audio(self):
        self.p.terminate()

audio = Audio()

@app.get("/alarme/{status}")
async def add_device(status: int):
    if status:audio.play_audio()
    else: audio.stop_audio()
    return {True}