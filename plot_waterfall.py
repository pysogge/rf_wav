# Program to read in a .wav file and plot a waterfall spectrogram image

import numpy as np
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt
from scipy import signal

# Wav file basename
basename = "29B6_IQ_20MHz_50Hz"

# Read the .wav file
rate, data = wav.read("iq_data/"+basename+".wav")

# Extract the I and Q samples
i_samples = data[:, 0]
q_samples = data[:, 1]

# Set the parameters for the STFT
nperseg = 512
noverlap = nperseg // 2

# Perform the STFT on the I and Q samples
f, t, Zxx = signal.stft(i_samples, fs=rate, nperseg=nperseg, noverlap=noverlap, return_onesided=False)

# Set the frequency and time limits for the plot based on the STFT parameters
f_start = -rate / 2
f_end = rate / 2
t_start = 0
t_end = t[-1]

# Plot the waterfall image
plt.pcolormesh(f, t, np.abs(Zxx).T, cmap='jet')
plt.title('STFT Magnitude - '+basename)
plt.xlabel('Frequency [Hz]')
plt.ylabel('Time [sec]')
plt.xlim(f_start, f_end)
plt.ylim(t_start, t_end)
plt.gca().invert_yaxis()
plt.show()


