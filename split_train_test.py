import os
import random

data_path = 'processed_wavs'

filename_list = os.listdir(data_path)
filename_list = list(map(lambda x: x.replace('.wav', ''), filename_list))
print(len(filename_list))
random.shuffle(filename_list)

train_filename = filename_list[:-512]
test_filename = filename_list[-512:]
print(len(train_filename))
print(len(test_filename))

for i in test_filename:
    assert i not in train_filename

with open('data/training.txt', 'w') as f:
    for i in train_filename:
        f.write(f'{i}||\n')

with open('data/validation.txt', 'w') as f:
    for i in test_filename:
        f.write(f'{i}||\n')