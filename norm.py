import os
import librosa
import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write as scipy_write

# Specify the directory containing audio files
audio_directory = '/workspaces/iitg_audio/Input folder'

# Specify the directory to save the refined audio files and plots
output_directory = '/workspaces/iitg_audio/Output'

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Iterate through all files in the directory
for file_name in os.listdir(audio_directory):
    # Construct the full path to the file
    file_path = os.path.join(audio_directory, file_name)

    # Check if the item is a file (not a subdirectory)
    if os.path.isfile(file_path):
        # Load the audio file
        x, sr = librosa.load(file_path, sr=16000, mono=True)
        x = x / max(abs(x))
        
        # Update the file name to save with '_refined' appended
        refined_file_name = file_name.replace('.wav', '_refined.wav')
        refined_file_path = os.path.join(output_directory, refined_file_name)
        
        # Save the refined audio using scipy
        scipy_write(refined_file_path, sr, (x * 32767).astype(np.int16))

        # Plot the audio waveform
        t = np.arange(0, len(x)) / sr
        plt.figure()
        plt.plot(t, x)
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude')
        plt.title('Audio Waveform')
        plt.savefig(os.path.join(output_directory, f'{refined_file_name}_waveform.png'))
        plt.close()

        print(f'Processed file: {file_name}, Saved as: {refined_file_name}')

print('Processing completed.')