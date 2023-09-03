from src.run_settings.base_logger import logger
from src.audio_file_functions.save_audio import audio_params
from pydub import AudioSegment


def audio_file_cutting(cut_time, cut_range) -> None:
    audio = AudioSegment.from_file(audio_params["AUDIO_PATH"])
    logger.debug(f"""Cutting audio file ---{audio_params["AUDIO_PATH"]}--- at timestamp: {cut_time[cut_range-1]}""")
    timestamp = cut_time[cut_range-1]*1000
    new_audio = audio[timestamp:]
    new_audio.export(audio_params["AUDIO_PATH"], format="wav")
