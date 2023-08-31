from threading import Event


class ThreadsHandler:
    def __init__(self):
        print("initializing eventhandler")
        self.stop_thread_recording = Event()
        self.stop_thread_listening = Event()
        self.stop_thread_transcription = Event()
        self.audio_file_updated = Event()


ThreadsManager = ThreadsHandler()
