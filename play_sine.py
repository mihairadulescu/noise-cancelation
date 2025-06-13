# test_sound.py
import numpy as np
import sounddevice as sd

fs = 44100               # rata de eșantionare
duration = 30            # durată în secunde
freq = 400               # frecvență semnal

t = np.linspace(0, duration, int(fs * duration), endpoint=False)
wave = 0.5 * np.sin(2 * np.pi * freq * t)

print("🔊 Redăm semnal de 400Hz timp de 30 secunde...")
sd.play(wave, samplerate=fs)
sd.wait()
print("✅ Sunet terminat.")
