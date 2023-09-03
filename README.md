Voice input widget
==============================

Application that enables pseudo-real-time voice inputting in any text field. To improve performance and lower memory and gpu requirements app uses Faster Whisper model which is Whisper model rewritten in C++. Pressing the button (default one of the function buttons on the mouse - configurable) starts recording from audio device (default audio device for the computer - configurable). Audio is recorded and transcripted while the button is pressed. For better accuracy app prints one sentence back, what allows to keep the correct context. Every time the sentence is printed the initial part of audio becomes unnecessary, so it's deleted according to end of sentence time stamps.


How to choose function button?
====================

Run a command to open Event Window then press desired button and read its name from terminal

:Check Events: `xev`

:Sample output: `ButtonRelease event, serial 37, synthetic NO, window 0x2c00001,
    root 0x910, subw 0x0, time 47100795, (122,110), root:(172,197),
    state 0x10, button 9, same_screen YES`

How to run the code?
====================

:Create env: `python3 -m venv /path/to/new/virtual/environment`

:Activate env: `source /path/to/new/virtual/environment`

:Install requirements: `pip install -r requirements.txt`

:Run script: `python3 /path/to/main.py --model --language --audio --button`


Project Organization
------------

	├── README.md          			<- The top-level README for developers using this project.
	│
	├── requirements.txt   			<- The requirements file for reproducing the analysis environment, e.g.
	│                         		generated with `pip freeze > requirements.txt`
	│
	├── setup.py           			<- makes project pip installable (pip install -e .) so src can be imported
	│
	├── src                			<- Source code for use in this project.
	│   ├── __init__.py    			<- Makes src a Python module
	│   │
	│   ├── audio_file_functions		<- Scripts handle audio recording
	│   │   └── __init__.py    		<- Makes audio_file_functions a Python module
	│   │   └── audio_setup.py		<- Gets audio devices ids and audio parameters
	│   │   └── cutting_audio.py		<- Used to cut unnecessary audio that has already been trascripted
	│   │   └── read_audio.py		<- Read data from .wav file
	│   │	└── save_audio.py		<- Save data as .wav file
	│   │
	│   ├── button_trigger			<- Handling recording trigger
	│   │   └── __init__.py    		<- Makes button_trigger a Python module
	│   │   └── click_function_button .py	<- Starting and stopping recording
	│   │
	│   ├── model        			<- Script to load model
	│   │   │── __init__.py    		<- Makes model a Python module
	│   │   └── model_loading.py		<- Model loading
	│   │
	│   ├── run_settings			<- App settings
	│   │   └── __init__.py    		<- Makes run_settings a Python module
	│   │   └── base_logger.py		<- Logger config
	│   │   └── data_parsing.py		<- Data parser config
	│   │
	│   ├── threads_handling		<- Handles threads
	│   │   └── __init__.py    		<- Makes threads_handling a Python module
	│   │   └── threads_handler.py		<- Threads and events manager
	│   │   	
	│   ├── voice_record			<- Voice recording
	│   │   └── __init__.py    		<- Makes voice_record a Python module
	│   │   └── voice_input.py		<- Handles audio recording
	│   │   	
	│   └── voice_to_text			<- Audio transcription
	│      └── __init__.py    		<- Makes voice_to_text a Python module
	│      └── voice_transcriptions.py	<- Creating text from audio



--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
