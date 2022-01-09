import matplotlib.pyplot as plt
import pyaudio
import numpy as np
from scipy import signal

FORMAT = pyaudio.paInt16
SAMPLEFREQ = 44100 # 44 kbps
FRAMESIZE = 1024 # each buffer contains 1024 samples
NOFFRAMES = 220
PATH = "eingangssignal_raw"
PATH_T = "referenzdatensatz"
PATH_W = "eingangssignal_win"


# oeffne stream
p = pyaudio.PyAudio()
print('running')

stream = p.open(format=FORMAT,channels=1,rate=SAMPLEFREQ,input=True,frames_per_buffer=FRAMESIZE)
data = stream.read(NOFFRAMES*FRAMESIZE)
decoded = np.fromstring(data, np.int)
stream.stop_stream()
stream.close()
p.terminate()

# plot decoded und decodedTriggered in einer Abb
# plt decodedTriggered in line 75
plt.figure(figsize=(9, 7))
plt.subplot(211)
xvalue = np.arange(0, len(decoded))
plt.plot(decoded)
plt.title("Grundperiode")
plt.xlabel("Zeit in s")
plt.ylabel("Amplitude")


print('done')


# 1b Triggerfunktion auf decoded angewendet
for i in range(len(decoded)):
    if decoded[i] > 15000000:
        start = i
        break

decodedTriggered = decoded[start:start+SAMPLEFREQ]


# window ueber alle referenz daten
windownmr = 171

windows = np.zeros((windownmr, 512))

schnitt = 256

gauss = signal.windows.gaussian(512, 4)


for y in range(0, windownmr):
    schnitt = schnitt - 256
    for x in range(0, 512):
        windows[y, x] = np.mean(np.abs(np.fft.fft(decodedTriggered[schnitt] * gauss)))
        schnitt = schnitt + 1

for y in range(0, windownmr):
    for x in range(0, 512):
        windows[y] = np.mean(windows[y, x])




# plot decodedTriggerd
# save untriggerd vgl mit triggerd
deltaT = 1 / SAMPLEFREQ
xvalue = np.arange(start, start+SAMPLEFREQ) * deltaT
plt.subplot(212)
plt.plot(decoded[start:start+SAMPLEFREQ])
plt.xlabel("Abtastpunkte")
plt.ylabel("Amplitude")
plt.savefig('untriggeredANDtriggered.png')


#1c fft auf triggered Signal fuer amplitudenspektrum
ffttriggerd = np.fft.fft(decodedTriggered)
specTriggered = np.abs(ffttriggerd)
plt.figure()
plt.plot(specTriggered)
plt.title('Amplitudenspektrum Triggerfunktion')
plt.xlabel('Abtastpunkte')
plt.ylabel('Amplitude')
plt.savefig('triggeredAmplitudenspektrum.png')

# fft auf eingangsignal fuer amplitudenspektrum
fft = np.fft.fft(decoded)
spec = np.abs(fft)
plt.figure()
plt.plot(spec)
plt.title('Amplitudenspektrum')
plt.xlabel('Abtastpunkte')
plt.ylabel('Amplitude')
plt.savefig('ungetriggeredAmplitudenspektrum.png')


# plot fuer windowed funktion
plt.figure()
plt.plot(windows)
plt.title('Amplitudenspektrum Fensterfunktion')
plt.xlabel('Abtastpunkte')
plt.ylabel('Amplitude')
plt.savefig('fensterAmplitudenspektrum.png')
