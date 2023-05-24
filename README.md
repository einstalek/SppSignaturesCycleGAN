## How to run
- Download signatures dataset and save it here, ./SPP/signatures

It should have two folders inside: forg and org

- Build Docker:

```docker build  -t spp .```

- Run Docker:

```docker run -v /local/path/for/checkpoints:/app/pytorch-CycleGAN-and-pix2pix/checkpoints -e WANDB_API_KEY="you-wandb-key" spp```