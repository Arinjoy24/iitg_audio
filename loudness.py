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

def plot_wav_loudness(wav_loudness, output_folder):
    plt.hist(wav_loudness, bins=20, edgecolor='black')
    plt.xlabel('Loudness (dB)')
    plt.ylabel('Count of WAV Files')
    plt.title('Loudness of WAV Files')
    plt.savefig(os.path.join(output_folder, 'loudness_histogram.png'))
    plt.close()

if __name__ == "__main__":
    folder_path = '/workspaces/iitg_audio/Output'
    output_folder = 'Loudness Histogram'
    
    # Check if the output folder exists, if not, create it
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Check if the folder exists
    if not os.path.exists(folder_path):
        print("Folder not found.")
        exit(1)
    
    wav_loudness = get_wav_loudness(folder_path)
    plot_wav_loudness(wav_loudness, output_folder)