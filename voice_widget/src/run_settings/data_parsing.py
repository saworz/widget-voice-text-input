import argparse

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

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("--model", type=str, default="medium", help=f"available models: {MODELS}")
parser.add_argument("--audio", type=int, default=None, help="audio input device")
parser.add_argument("--gpu", type=bool, default=True, help="True for gpu, False for cpu")
parser.add_argument("--button", type=str, default="Button.button9", help="button used to control voice recording")
opt = parser.parse_args()
