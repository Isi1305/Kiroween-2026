import numpy as np
from scipy.io import wavfile
from pydub import AudioSegment

# calculate frequency
sample_rate = 44100
duration = 2 # seconds

t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

tone_1 = np.sin(2 * np.pi * 853 * t)
tone_2 = np.sin(2 * np.pi * 960 * t)
tone = tone_1 + tone_2 # put the frequency together
tone = tone / np.max(np.abs(tone)) * 0.5 # save volume

wavfile.write("assets/alarm.wav", sample_rate, (tone * 32767).astype(np.int16))

tone = AudioSegment.from_file("assets/alarm.wav")
voice = AudioSegment.from_file("warning.mp3")

final = tone + voice + tone
final.export("test_final.mp3", format="mp3")