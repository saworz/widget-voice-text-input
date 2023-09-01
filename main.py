import sys
import os
from pathlib import Path

BASE_DIR = Path(__file__)
module_path = BASE_DIR.parent
if module_path not in sys.path:
    sys.path.append(str(module_path))

from src.button_trigger.click_function_button import listen_thread


def main() -> None:
    listen_thread()


if __name__ == "widget.main":
    main()
