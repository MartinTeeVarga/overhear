# Overhear
Threshold voice chat activation for Blizzard's Overwatch. It automatically presses the back tick key ` when a configured noise level is reached. It releases the key after one second of silence.

## Installation
* Install Python 2.7+. Might work with Python 3 but not tested.
* Run the following two commands to install libraries:
    * pip install pyaudio
    * pip install pypiwin32

## Running
Run the following command:
* python overhear.py

Terminate the program by pressing CTRL+C.

## Configuration
If the preset threshold is too low or too high, edit the overhear.py script and change the variable THRESHOLD to a different number. The higher it is, the louder the noise must be to activate the key press.




