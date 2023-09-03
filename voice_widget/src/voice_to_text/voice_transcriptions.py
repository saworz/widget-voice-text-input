from src.audio_file_functions.read_audio import get_data_from_audio_file
from src.audio_file_functions.cutting_audio import audio_file_cutting
from src.threads_handling.threads_handler import ThreadsManager
from src.model.model_loading import load_model
import pyautogui
import re
import numpy as np

model = load_model()


def get_sentences(segments: iter) -> tuple[list[str], list[float]]:
    END_OF_SENTENCE_CHAR = ['!', '...', '.', '?']
    sentences = []
    new_sentence_timestamps = []
    current_sentence = ''
    text = ''

    for segment in segments:
        for word in segment.words:
            for delimiter in END_OF_SENTENCE_CHAR:
                if delimiter in word.word:
                    new_sentence_timestamps.append(word.end)
                    break

            text += word.word

    result = re.split(r'([.?!]+|\.{3})', text)

    for i, fragment in enumerate(result):
        if i % 2 == 0:
            current_sentence += fragment
        else:
            current_sentence += fragment
            sentences.append(current_sentence.strip())
            current_sentence = ''

    return sentences, new_sentence_timestamps


def transcribe(data: np.ndarray) -> None:
    segments, _ = model.transcribe(audio=data, language='en', word_timestamps=True)
    sentences, new_sentence_times = get_sentences(segments)

    if len(sentences) > 1:
        cut_range = len(sentences) - 1
        audio_file_cutting(new_sentence_times, cut_range)
        sentences_to_print = sentences[:cut_range]

        for sentence in sentences_to_print:
            pyautogui.typewrite(sentence)
            pyautogui.typewrite(' ')


def transcribe_leftover_audio(data: np.ndarray) -> None:
    segments, _ = model.transcribe(audio=data, language='en', word_timestamps=True)
    final_text = []

    for segment in segments:
        for word in segment.words:
            final_text.append(word.word)

    final_text = ''.join(final_text)[1:]
    pyautogui.typewrite(final_text)


def run_transcription() -> None:
    while True:
        if ThreadsManager.stop_thread_transcription.is_set():
            transcribe_leftover_audio(get_data_from_audio_file())
            break

        if ThreadsManager.audio_file_updated.is_set():
            transcribe(get_data_from_audio_file())
            ThreadsManager.audio_file_updated.clear()
