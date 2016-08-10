import audioop
import sys
import time
# install using "pip install pyaudio"
import pyaudio
#install using "pip install pypiwin32"
import win32api
import win32con

chunk = 1024
#threshold depends on headphones, need experimentation
#set, run the script, talk and watch the "key on/off" message
THRESHOLD = 768

p = pyaudio.PyAudio()

stream = p.open(format=pyaudio.paInt16,
                channels=1,
                rate=44100,
                input=True,
                frames_per_buffer=chunk)
try:
    stamp = None

    while True:
        data = stream.read(chunk)
        rms = audioop.rms(data, 2)
        if rms >= THRESHOLD:
            win32api.keybd_event(0xC0, 0, 0, 0)
            stamp = time.time()
            sys.stdout.write("\rKey on  %i   " % rms)
            sys.stdout.flush()
        elif stamp and time.time() - stamp > 1 and rms < THRESHOLD:
            win32api.keybd_event(0xC0, 0, win32con.KEYEVENTF_KEYUP, 0)
            stamp = None
            sys.stdout.write("\rKey off %i   " % rms)
            sys.stdout.flush()


except KeyboardInterrupt:
    stream.stop_stream()
    stream.close()
    p.terminate()
