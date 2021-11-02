import pyaudio
import numpy as np
from boxing import boxing
class werno:
    biasa = "\033[1;37m"
    abang = "\033[1;31m"
    ijo = "\033[1;32m"
    kuning = "\033[0;33m"
    biru = "\033[1;34m"
    hasil = "\033[1;37;42m"
    merah_putih = "\033[1;37;41m"
    njambon = "\033[1;33m"
    normal = "\033[0;37;40m"

maxValue = 2**16
p=pyaudio.PyAudio()
stream=p.open(format=pyaudio.paInt16,channels=2,rate=44100,
              input=True, frames_per_buffer=1024)
while True:
    data = np.fromstring(stream.read(1024),dtype=np.int16)
    dataL = data[0::2]
    dataR = data[1::2]
    peakL = np.abs(np.max(dataL)-np.min(dataL))/maxValue
    peakR = np.abs(np.max(dataR)-np.min(dataR))/maxValue
    xx = round(peakL*10000)
    yy = round(peakR*10000)
    print(werno.biru+"#"*xx)
    print(werno.ijo+"#"*yy)
    # print("L:%00.02f R:%00.02f"%(peakL*100, peakR*100))
