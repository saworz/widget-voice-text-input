from src.run_settings.data_parsing import opt
import pyaudio
import logging
import sounddevice


def get_audio_parameters(display: bool) -> dict:
    dev_audio_index = 0
    p = pyaudio.PyAudio()

    if opt.audio is None:
        for i in range(p.get_device_count()):
            dev_inf = p.get_device_info_by_index(i)
            filtered_dict = {key: value for key, value in dev_inf.items() if key in ('index', 'name', 'maxInputChannels')}

            if display:
                print(filtered_dict)

            if dev_inf['name'] == 'default':
                dev_audio_index = dev_inf['index']

    else:
        dev_audio_index = opt.audio

    logging.info(f"Audio device index: {dev_audio_index}")
    audio_params = {"CHANNELS": 1,
                    "FRAME_RATE": 16000,
                    "RECORD_SECONDS": 1,
                    "AUDIO_FORMAT": pyaudio.paInt16,
                    "SAMPLE_SIZE": 2,
                    "CHUNK": 1024,
                    "audio_device_index": dev_audio_index,
                    "AUDIO_PATH": "recorded_audio.wav"}

    return audio_params
