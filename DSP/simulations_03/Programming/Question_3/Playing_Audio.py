from scipy.io import wavfile

import sounddevice as sd
sd._terminate()
sd._initialize()
playfile='amy.wav'
fs,data=wavfile.read(playfile)
sd.play(data,80000,blocking=True)

