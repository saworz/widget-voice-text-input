from src.run_settings.base_logger import logger
from src.run_settings.data_parsing import opt
import torch
from faster_whisper import WhisperModel


def load_model() -> WhisperModel:
    if opt.gpu:
        if torch.cuda.is_available():
            device = "cuda"
        else:
            device = "cpu"
            logger.warning("torch cuda not available, using cpu")
    else:
        device = "cpu"

    logger.info("Loading model...")
    model = WhisperModel(opt.model, device=device, compute_type="int8")
    logger.info(f"Model ---{opt.model}--- loaded on ---{device}---")
    return model
