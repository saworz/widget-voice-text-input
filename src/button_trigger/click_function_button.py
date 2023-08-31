from src.run_settings.base_logger import logger
from src.threads_handling.threads_handler import ThreadsManager
from src.voice_record.voice_input import record_microphone
from pynput.mouse import Listener
from threading import Thread


def click_function_button(x, y, button, pressed) -> bool:
    """Handles function button click"""
    fn_button = 'Button.button9'
    if ThreadsManager.stop_thread_listening.is_set():
        return False

    if str(button) == fn_button:
        if pressed:
            logger.debug("Starting recording")
            ThreadsManager.stop_thread_recording.clear()
            ThreadsManager.stop_thread_transcription.clear()
            Thread(target=record_microphone).start()
            return True

        logger.debug("Stopping recording...")
        ThreadsManager.stop_thread_recording.set()
        return False


def listen_thread() -> None:
    # while not ThreadsManager.stop_thread_listening.is_set():
    while True:
        with Listener(on_click=click_function_button) as listener:
            listener.join()
