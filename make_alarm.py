from pydub import AudioSegment
import numpy as np
from scipy.io import wavfile

# calculate frequency
sample_rate = 44100
duration = 2 # seconds

t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

tone = np.sin(2 * np.pi * 853 * t)
tone = tone / np.max(np.abs(tone)) * 0.5 # save volume

wavfile.write("assets/alarm.wav", sample_rate, (tone * 32767).astype(np.int16))