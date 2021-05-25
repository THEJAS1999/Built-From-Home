import numpy as np
import librosa
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

style.use('fivethirtyeight')
sr=0
aud= 'Leave.mp3'
# filename = librosa.ex('Leave')
y, sr = librosa.load(aud, sr=44100)
print(y)
print(sr)
y_ps = librosa.effects.pitch_shift(y, sr, n_steps=6)
y_ts = librosa.effects.time_stretch(y, rate=1.2)
plt.subplot(311)
plt.plot(y)
plt.title('Original waveform')
plt.axis([0, 200000, -0.4, 0.4])
# plt.axis([88000, 94000, -0.4, 0.4])
plt.subplot(312)
plt.plot(y_ts)
plt.title('Time Stretch transformed waveform')
plt.axis([0, 200000, -0.4, 0.4])
plt.subplot(313)
plt.plot(y_ps)
plt.title('Pitch Shift transformed waveform')
plt.axis([0, 200000, -0.4, 0.4])
# plt.axis([88000, 94000, -0.4, 0.4])
plt.tight_layout()
plt.show() 