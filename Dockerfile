FROM ubuntu:focal
# Use an official Python runtime as the base image
FROM python:3.9-slim-buster

# Install git
RUN apt-get update && apt-get install -y git gcc python3-dev

# Set the working directory in the container to /app
WORKDIR /app

# Clone cycle-gan git repository
RUN git clone https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix

# Install the required libraries
RUN pip install -r pytorch-CycleGAN-and-pix2pix/requirements.txt

# Update networks.py containing SPP Discriminator
COPY networks.py pytorch-CycleGAN-and-pix2pix/models/

# Create train/test dataset split, mount path to signatures at /data
COPY train_test_split.py /app
CMD ["python", "/app/train_test_split.py", "/data"]

COPY auth_wandb.py /app
CMD ["python", "auth_wandb.py"]

WORKDIR /app/pytorch-CycleGAN-and-pix2pix/
CMD ["python", "train.py", \
    "--dataroot", "/app/split", \
    "--name", "forg2org", \
    "--model", "cycle_gan", \
    "--netD", "spp", \
    "--batch_size", "4", \
    "--display_id", "-1", \
    "--wandb_project_name", "cycle_gan_signatures", \
    "--use_wandb"]




