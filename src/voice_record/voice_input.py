from src.audio_file_functions.save_audio import audio_params
from src.audio_file_functions.save_audio import init_audio_file, write_audio_to_file
from src.voice_to_text.voice_transcriptions import run_transcription
from src.threads_handling.threads_handler import ThreadsManager
from threading import Thread
import pyaudio


def handle_data_stream(stream):

    for i in range(0, int(audio_params["FRAME_RATE"] / audio_params["CHUNK"] * audio_params["RECORD_SECONDS"])):
        data = stream.read(audio_params["CHUNK"])

        write_audio_to_file(data)
        ThreadsManager.audio_file_updated.set()


def record_microphone() -> None:
    p = pyaudio.PyAudio()
    stream = p.open(format=audio_params["AUDIO_FORMAT"],
                    channels=audio_params["CHANNELS"],
                    rate=audio_params["FRAME_RATE"],
                    input=True,
                    input_device_index=audio_params["audio_device_index"],
                    frames_per_buffer=audio_params["FRAME_RATE"])

    Thread(target=run_transcription).start()
    init_audio_file()

    while True:
        handle_data_stream(stream)
        if ThreadsManager.stop_thread_recording.is_set():
            break

    stream.stop_stream()
    stream.close()
    p.terminate()
    ThreadsManager.stop_thread_transcription.set()
