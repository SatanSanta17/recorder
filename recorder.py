import sounddevice
from scipy.io.wavfile import write
from datetime import *
import os.path
fs = 44100
second = int(input("Enter the time duration in seconds: "))
print("recording.....\n")
record_voice = sounddevice.rec(int(second*fs), samplerate=fs, channels=2)
sounddevice.wait()
now = datetime.now()
current_time = now.strftime("%H%M%S")
# folder = './recordings/'
# fileName = "{today}.wav".format(today=current_time)
# file_path = os.path.join(folder, fileName)
# if not os.path.isdir(folder):
#     os.mkdir(folder)
# recording = open(file_path, "w")
write("{today}.wav".format(today=current_time), fs, record_voice)
print("finished......\n please check")
