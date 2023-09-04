from setuptools import find_packages, setup
from pathlib import Path
import sys

BASE_DIR = Path(__file__).parent
module_path = BASE_DIR / "source" / "src"

if module_path not in sys.path:
	sys.path.append(module_path)
	
with open(Path(BASE_DIR, "requirements.txt")) as file:
    required_packages = [ln.strip() for ln in file.readlines()]

setup(
    name='voice_widget',
    packages=find_packages(),
    version='1.0',
    entry_points={'console_scripts': ['voice_widget=voice_widget.main']},
    description='Voice transcription',
    author='Michal',
    data_files=[('voice_widget/src/run_settings', ['voice_widget/src/run_settings/config.ini'])],
    install_requires=[required_packages],
)
