import pyaudio
import numpy as np


FORMAT = pyaudio.paInt16
SAMPLEFREQ = 44100 # 44 kbps
FRAMESIZE = 1024 # each buffer contains 1024 samples
NOFFRAMES = 220
PATH = "eingangssignal_raw"
PATH_T = "referenzdatensatz"
PATH_W = "eingangssignal_win"
PATH_G = "sprechergina"
PATH_L = "sprecherluca"

p = pyaudio.PyAudio()
print('running')
# 1a open stream
stream = p.open(format=FORMAT,channels=1,rate=SAMPLEFREQ,input=True,frames_per_buffer=FRAMESIZE)
data = stream.read(NOFFRAMES*FRAMESIZE)
decoded = np.fromstring(data, np.int)
stream.stop_stream()
stream.close()
p.terminate()

# 1b Triggerfunktion auf decoded angewendet
for i in range(len(decoded)):
    if decoded[i] > 15000000:
        start = i
        break

decodedTriggered = decoded[start:start+SAMPLEFREQ]

def safeTriggeredAsCSV(eingangssignal):
    csvTrigArray = np.savetxt(PATH_T + "/decodedtrigL1.csv", eingangssignal, delimiter=",")
    return csvTrigArray


safeTriggeredAsCSV(decodedTriggered)

print('done')
