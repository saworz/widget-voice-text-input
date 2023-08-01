# from src.streamlit_ui.user_interface import create_ui
# import torch
# import whisper
# import streamlit as st
# from time import time
import pyaudio
import pyautogui
from pynput.mouse import Listener
from collections import deque
import pyaudio
import wave
import sounddevice
from threading import Thread, Event

true_text = 'My dear Fanny, you feel these things a great deal too much. I am most happy that you like the chain'

"""
@st.cache_resource
def load_model(model_size: str):
    return whisper.load_model(model_size)


def main() -> None:
    # Set inference device
    create_ui()
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    model = load_model('tiny').to(device)
    start = time()
    text = model.transcribe("data/sample.mp3")
    end = time()
    print(text)
    print(f"total time: {end-start}")
"""

stop_condition = Event()


def click_function_button(x, y, button, pressed):
    """Handles function button click"""
    fn_button = 'Button.button9'

    if str(button) == fn_button:
        if pressed:
            # pyautogui.click(x, y)
            # pyautogui.typewrite("hello There!!!")
            print("listening channel")
            stop_condition.clear()
            Thread(target=record_microphone).start()
            # record_microphone()

            return True
        if not pressed:
            print("abort listening")
            stop_condition.set()
            return False


CHANNELS = 1
FRAME_RATE = 16000
RECORD_SECONDS = 20
AUDIO_FORMAT = pyaudio.paInt16
SAMPLE_SIZE = 2
transcript = deque()
records = deque()
SECONDS = 3
CHUNK = 1024


def record_microphone():
    p = pyaudio.PyAudio()

    stream = p.open(format=AUDIO_FORMAT,
                    channels=CHANNELS,
                    rate=FRAME_RATE,
                    input=True,
                    input_device_index=6,
                    frames_per_buffer=CHUNK)

    frames = []

    for i in range(0, int(FRAME_RATE / CHUNK * SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

        if stop_condition.is_set():
            break

    stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    p.terminate()
    print('terminated')
    # while not len(records) == 0:
    #     data = stream.read(chunk)
    #     frames.append(data)
    #     print(data)
    #     if len(frames) >= (FRAME_RATE * RECORD_SECONDS) / chunk:
    #         print(frames.copy())
    #         records.append(frames.copy())
    #         frames = []


if __name__ == '__main__':
    # main()
    while True:
        with Listener(on_click=click_function_button) as listener:
            listener.join()