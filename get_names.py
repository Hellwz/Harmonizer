import os

file_path = r"./docs/audio/val"
names = []

for root, dirs, files in os.walk(file_path):
    for audio_full_name in files:
        if os.path.splitext(audio_full_name)[1] != '.mp3': continue
        names.append(audio_full_name[: -4])

print(names)