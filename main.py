import numpy as np
import sounddevice as sd

# Parametri de configurare
duration = 10          # Durata totală în secunde
samplerate = 44100     # Eșantionare audio
channels = 1           # Mono
blocksize = 1024       # Mărimea blocului de procesare

def anc_callback(indata, outdata, frames, time, status):
    if status:
        print(f"⚠️ Status stream: {status}")
    # Emitere anti-sunet (fază inversă)
    outdata[:] = -indata

print("🔊 Noise cancellation activ timp de 10 secunde...")

try:
    with sd.Stream(
        channels=channels,
        samplerate=samplerate,
        blocksize=blocksize,
        callback=anc_callback
    ):
        sd.sleep(int(duration * 1000))
except Exception as e:
    print(f"❌ Eroare: {e}")
