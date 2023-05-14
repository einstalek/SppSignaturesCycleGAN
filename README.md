## How to run
- Download signatures dataset and save it locally

- Build Docker:

```docker build  -t spp .```

- Run Docker:

```docker run -v /path/to/signatures/:/data -v /local/path/for/checkpoints:/app/pytorch-CycleGAN-and-pix2pix/checkpoints -e WANDB_API_KEY="you-wandb-key" spp```