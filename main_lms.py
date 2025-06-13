# main_lms.py
import numpy as np
import sounddevice as sd
import padasip as pa

fs = 44100               # rata de eșantionare
blocksize = 1024
duration = 30
freq = 400               # frecvența cunoscută a semnalului din Laptop A
mu = 0.001               # rată învățare LMS
delay = 32               # delay artificial (în sample-uri)
gain = 0.5               # scalare anti-sunet

lms_filter = pa.filters.FilterLMS(n=blocksize, mu=mu)

print("🎯 Noise cancellation LMS pornit – anulăm DOAR semnalul de 400Hz din Laptop A...")

def callback(indata, outdata, frames, time, status):
    if status:
        print("⚠️", status)

    # referință: semnal cunoscut, shiftat puțin pentru compensare delay
    t = np.arange(blocksize) / fs
    ref = 0.5 * np.sin(2 * np.pi * freq * t)
    ref = np.roll(ref, delay)

    mic = indata[:, 0]                    # semnal real captat
    y_hat = lms_filter.predict(ref)      # estimare componentă ce trebuie anulată
    error = mic - y_hat                  # zgomot curat
    lms_filter.adapt(error, ref)

    anti = -gain * np.clip(y_hat, -1.0, 1.0)  # anti-sunet
    outdata[:, 0] = anti

with sd.Stream(channels=1, samplerate=fs, blocksize=blocksize, callback=callback):
    sd.sleep(int(duration * 1000))

print("✅ Noise cancellation LMS terminat.")
