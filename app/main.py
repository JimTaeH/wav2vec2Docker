from fastapi import FastAPI, UploadFile
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import torchaudio
from .processAudio import preparedArrayandSampleRate, blike2b
from .inference import stt
import numpy as np

app = FastAPI()

@app.post("/stt", tags=["wav2vec2"])
def stt_onserver(audioFile: UploadFile):
    fileExtension = audioFile.filename.split(".")[1]
    rawData = audioFile.file.read()
    audio = blike2b(blike=rawData)
    audioData, sr = torchaudio.load(audio, format=fileExtension)

    if sr >= 16000:
        audioData16k, sr16k = preparedArrayandSampleRate(audioData=audioData, sr=sr)
    
    text = stt(audioData=audioData16k, sr=sr16k)
    text = {"text": text}

    return JSONResponse(content=jsonable_encoder(text))

