import numpy as np
import sounddevice as sd

duration = 10  # secunde
frequency = 400  # Hz
samplerate = 44100

t = np.linspace(0, duration, int(samplerate * duration), endpoint=False)
wave = 0.5 * np.sin(2 * np.pi * frequency * t)

print("🔈 Redare sunet test (400Hz)...")
sd.play(wave, samplerate)
sd.wait()
