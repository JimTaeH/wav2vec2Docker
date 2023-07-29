import torchaudio
from io import BytesIO

def preparedArrayandSampleRate(audioData=None, sr=None):
    sr16k = 16000
    audioData16k = torchaudio.functional.resample(audioData, orig_freq=sr, new_freq=sr16k)
    
    if audioData16k.shape[0] > 1:
      audioData16k = audioData16k[0].reshape(1, -1)

    return [audioData16k, sr16k]

def blike2b(blike=None):
  bObj = BytesIO(blike)

  return bObj