import os
import parselmouth
import matplotlib.pyplot as plt

def get_wav_loudness(folder_path):
    wav_loudness = []

    for filename in os.listdir(folder_path):
        if filename.endswith(".wav"):
            file_path = os.path.join(folder_path, filename)
            snd = parselmouth.Sound(file_path)
            loudness = snd.to_intensity().values.T[1]  # Get loudness values
            mean_loudness = sum(loudness) / len(loudness)  # Mean loudness for the file
            wav_loudness.append(mean_loudness)

    return wav_loudness

def plot_wav_loudness(wav_loudness):
    plt.hist(wav_loudness, bins=20, edgecolor='black')
    plt.xlabel('Loudness (dB)')
    plt.ylabel('Frequency')
    plt.title('Loudness of WAV Files')
    plt.show()

if __name__ == "__main__":
    folder_path = 'C:/Users/arinj/Downloads/Histogram (Loudness)'
    wav_loudness = get_wav_loudness(folder_path)
    plot_wav_loudness(wav_loudness)
