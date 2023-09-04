import argparse
import configparser
import os


def int_or_none(value):
    if value.lower() == 'none':
        return None
    try:
        return int(value)
    except ValueError:
        raise argparse.ArgumentTypeError(f"'{value}' is not a valid integer or 'none'")


def str_to_bool(value):
    if isinstance(value, bool):
        return value
    if value.lower() in ('true', 'yes', '1'):
        return True
    elif value.lower() in ('false', 'no', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError(f"Invalid boolean value: {value}")


MODELS = (
    "tiny.en",
    "tiny",
    "base.en",
    "base",
    "small.en",
    "small",
    "medium.en",
    "medium",
    "large-v1",
    "large-v2",
)

this_folder = os.path.dirname(os.path.abspath(__file__))
config = configparser.ConfigParser()
config_path = os.path.join(this_folder, "config.ini")
config.read(config_path)

config_model = config.get("Config", "model")
config_audio = config.get("Config", "audio")
config_gpu = config.get("Config", "gpu")
config_button = config.get("Config", "button")

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("--model", type=str, default=config_model, help=f"Available models: {MODELS}")
parser.add_argument("--audio", type=int_or_none, default=config_audio, help="Audio input device")
parser.add_argument("--gpu", type=str_to_bool, default=config_gpu, help="True for gpu, False for cpu")
parser.add_argument("--button", type=str, default=config_button, help="Button used to control voice recording")
opt = parser.parse_args()

config.set("Config", "model", opt.model)
config.set("Config", "audio", str(opt.audio))
config.set("Config", "gpu", str(opt.gpu))
config.set("Config", "button", opt.button)

with open(config_path, "w") as config_file:
    config.write(config_file)
