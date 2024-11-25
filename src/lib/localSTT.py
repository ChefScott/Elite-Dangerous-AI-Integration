import io
import time
from pywhispercpp.model import Model
import samplerate
import soundfile as sf

stt_models_names = [
    'distil-medium.en',
    'distil-small.en', 

    'tiny', 
    'tiny.en', 
    'base', 
    'base.en',
    'small', 
    'small.en', 
    'medium', 
    'medium.en', 
    'large-v1',
    'large-v2', 
    'large-v3', 
    'large', 
    'distil-large-v2',
    'distil-large-v3',
]

def init_stt(model_name="distil-medium.en"):
    model = Model(model_name)
    return model

def stt(model: Model, wav: bytes, language="en-US"):
    # convert wav bytes to 16k S16_LE

    start = time.time()
    audio, rate = sf.read(io.BytesIO(wav))
    end = time.time()
    print("Read time:", end - start)
    start = time.time()
    audio = samplerate.resample(audio, 16000 / rate, 'sinc_best')
    end = time.time()
    print("Resample time:", end - start)

    start = time.time()
    segments = model.transcribe(audio)
    #gen, info = model.transcribe(audio)
    #
    #segments = []
    #for segment in gen:
    #    segments.append(segment)
    
    end = time.time()
    print("Transcribe time:", end - start)
    
    return segments, None