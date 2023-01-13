import librosa
import shutil
import os


def filter_by_audio_length(source_path, destination_path, min_length=6.0):
    filenames = os.listdir(source_path)
    for filename in filenames:
        source_file_path = os.path.join(source_path, filename)
        if os.path.isfile(source_file_path):
            waveform, sr = librosa.load(source_file_path)
            if librosa.get_duration(y=waveform, sr=sr) >= min_length:
                destination_file_path = os.path.join(destination_path, filename)
                shutil.copyfile(source_file_path, destination_file_path)
                print(f"Copied {source_file_path} to {destination_file_path}.")


source_path = "processed_wavs_22050_norm"
destination_path = "test_files"
filter_by_audio_length(source_path, destination_path, 26.0)