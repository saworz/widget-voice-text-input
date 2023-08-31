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