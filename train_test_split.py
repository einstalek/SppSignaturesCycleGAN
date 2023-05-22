import glob
import os
import os.path as osp
import sys
import random
from shutil import copyfile

if __name__ == "__main__":
    dataset_root = sys.argv[1]

    for fold in ('trainA', 'testA', 'trainB', 'testB'):
        os.makedirs(osp.join("/app", "split", fold), exist_ok=True)
    
    
    a_fps = glob.glob(os.path.join(dataset_root, 'forg', '*.png'))
    b_fps = glob.glob(os.path.join(dataset_root, 'org', '*.png'))

    for fps, sub in [(a_fps, 'A'), (b_fps, 'B')]:
        train_size = int(0.9 * len(fps))
        random.shuffle(fps)
        train_fps, test_fps = fps[:train_size], fps[train_size:]

        for fp in train_fps:
            destination_path = os.path.join('/app', 'split', 'train' + sub, os.path.basename(fp))
            copyfile(fp, destination_path)
        for fp in test_fps:
            destination_path = os.path.join('/app', 'split', 'test' + sub, os.path.basename(fp))
            copyfile(fp, destination_path)
