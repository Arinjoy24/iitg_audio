import librosa
import numpy as np
import matplotlib.pyplot as plt
path_to_save = 'C:/Users/arinj/Downloads/Audio'
for file_name in ["C:/Users/arinj/Downloads/Old Audio"]:
    x, sr = librosa.load(file_name, sr=16000, mono=True)
    x = x/max(abs(x))
    file_name = file_name + '_refined'
    librosa.write(file_name, x, sr)
t = np.arange(0, len(x)) / sr
fig, ax = plt.subplots(1, 1, figsize=[8, 3])
ax.plot(t, x)
plt.show()