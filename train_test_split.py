import glob
import os
import os.path as osp
import sys
import random
from shutil import copyfile

if __name__ == "__main__":
    split_root = "/app/split/"  # where to create split folders

    for fold in ('trainA', 'testA', 'trainB', 'testB'):
        fold_fp = osp.join(split_root, fold)
        os.makedirs(fold_fp, exist_ok=True)

    # take files from /app/data/
    a_fps = glob.glob(os.path.join('/app/data/', 'forg', '*.png'))
    b_fps = glob.glob(os.path.join('/app/data/', 'org', '*.png'))

    for fps, sub in [(a_fps, 'A'), (b_fps, 'B')]:
        train_size = int(0.9 * len(fps))
        random.shuffle(fps)
        train_fps, test_fps = fps[:train_size], fps[train_size:]

        for fp in train_fps:
            dst_fp = osp.join(split_root, f"train{sub}", os.path.basename(fp))
            copyfile(fp, dst_fp)
        for fp in test_fps:
            dst_fp = osp.join(split_root, f"test{sub}", os.path.basename(fp))
            copyfile(fp, dst_fp)
