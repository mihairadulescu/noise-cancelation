# main.py
import numpy as np
import sounddevice as sd

fs = 44100               # rata de eșantionare
blocksize = 1024
duration = 30
gain = 0.3               # scalare anti-sunet (evită feedback)

print("🔇 Noise cancellation pasiv pornit (fază inversă)...")

def callback(indata, outdata, frames, time, status):
    if status:
        print("⚠️", status)

    outdata[:, 0] = -gain * np.clip(indata[:, 0], -1.0, 1.0)

with sd.Stream(channels=1, samplerate=fs, blocksize=blocksize, callback=callback):
    sd.sleep(int(duration * 1000))

print("✅ Noise cancellation terminat.")
