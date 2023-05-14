## How to run
- Download signatures dataset and save it locally

- Build Docker:

```docker build  -t spp .```

- Run Docker:

```docker run -v /path/to/signatures/:/data -e WANDB_API_KEY="you-wandb-key" spp```