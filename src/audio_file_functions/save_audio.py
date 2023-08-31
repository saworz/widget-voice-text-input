from src.audio_file_functions.audio_setup import get_audio_parameters
import wave

audio_params = get_audio_parameters(display=False)


def set_audio_params(file: wave.Wave_write) -> None:
    file.setnchannels(audio_params["CHANNELS"])
    file.setsampwidth(audio_params["SAMPLE_SIZE"])
    file.setframerate(audio_params["FRAME_RATE"])


def init_audio_file() -> None:
    with wave.open(audio_params["AUDIO_PATH"], 'wb') as wf:
        set_audio_params(wf)


def write_audio_to_file(data: bytes) -> None:

    with wave.open(audio_params["AUDIO_PATH"], 'rb') as existing_wf:
        existing_data = existing_wf.readframes(existing_wf.getnframes())

    with wave.open(audio_params["AUDIO_PATH"], 'wb') as new_wf:
        set_audio_params(new_wf)
        new_wf.writeframes(existing_data)
        new_wf.writeframes(data)
