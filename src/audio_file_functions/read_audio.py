import numpy as np
from src.audio_file_functions.save_audio import audio_params


def get_data_from_audio_file():
    with open(audio_params["AUDIO_PATH"], 'rb') as fd:
        contents = fd.read()

    return np.frombuffer(contents, np.int16).flatten().astype(np.float32) / 32768.0
