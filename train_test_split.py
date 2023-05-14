import glob
import os
import sys
import random
from shutil import copyfile

if __name__ == "__main__":
    dataset_root = sys.argv[1]

    for fold in ('trainA', 'testA', 'trainB', 'testB'):
        os.makedirs(f'/app/split/{fold}', exist_ok=True)

    a_fps = glob.glob(f'{dataset_root}/full_forg/*.png')
    b_fps = glob.glob(f'{dataset_root}/full_org/*.png')

    for fps, sub in [(a_fps, 'A'), (b_fps, 'B')]:
        train_size = int(0.9 * len(fps))
        random.shuffle(fps)
        train_fps, test_fps = fps[:train_size], fps[train_size:]

        for fp in train_fps:
            copyfile(fp, f'/app/split/train{sub}/{os.path.basename(fp)}')
        for fp in test_fps:
            copyfile(fp, f'/app/split/test{sub}/{os.path.basename(fp)}')
