

## Environment Dependencies

Our code is built on Huggingface Diffusers (0.22.0), please follow [sdxl](https://github.com/huggingface/diffusers/blob/v0.22.0-release/examples/dreambooth/README_sdxl.md) for environment setup.


### Install B4M
```bash
cd B4M
pip install -e .
```


## Training Instructions

The training process include two stages.

### Stage One: Train Content and Style Separately

- **Train the content model**  
  Run the following script:

  ```bash

  bash code/train_content.sh
  ```

- **Train the style model**  
  Run the following script:

  ```bash
  bash code/train_style.sh
  ```

> Note: In both scripts, please replace any dataset paths, output directories, and other file paths with your own.

### Stage Two: Joint Training with Riemannian Precondition

After completing the first stage, run the following script to start the second-stage training:

```bash
bash code/train_second_stage.sh
```

> As before, make sure to update the paths in the script to fit your environment.

## Inference

After training is complete, you can run inference using:

```bash
python infer.py
```

Make sure to configure the model path and input settings inside the script as needed.


## TODO List

- [x] Open source the code  
- [ ] Upload the checkpoints used in the paper examples  



Check out the [Quickstart](https://huggingface.co/docs/diffusers/quicktour) to launch your diffusion journey today!

## How to navigate the documentation


</table>

## Popular libraries using 🧨 Diffusers

- https://github.com/microsoft/TaskMatrix
- https://github.com/invoke-ai/InvokeAI
- https://github.com/apple/ml-stable-diffusion
- https://github.com/Sanster/lama-cleaner
- https://github.com/IDEA-Research/Grounded-Segment-Anything
- https://github.com/ashawkey/stable-dreamfusion
- https://github.com/deep-floyd/IF
- https://github.com/bentoml/BentoML
- https://github.com/bmaltais/kohya_ss
- +3000 other amazing GitHub repositories 💪

Thank you for using us ❤️

## Credits

This library concretizes previous work by many different authors and would not have been possible without their great research and implementations. We'd like to thank, in particular, the following implementations which have helped us in our development and without which the API could not have been as polished today:

- @CompVis' latent diffusion models library, available [here](https://github.com/CompVis/latent-diffusion)
- @hojonathanho original DDPM implementation, available [here](https://github.com/hojonathanho/diffusion) as well as the extremely useful translation into PyTorch by @pesser, available [here](https://github.com/pesser/pytorch_diffusion)
- @ermongroup's DDIM implementation, available [here](https://github.com/ermongroup/ddim)
- @yang-song's Score-VE and Score-VP implementations, available [here](https://github.com/yang-song/score_sde_pytorch)

We also want to thank @heejkoo for the very helpful overview of papers, code and resources on diffusion models, available [here](https://github.com/heejkoo/Awesome-Diffusion-Models) as well as @crowsonkb and @rromb for useful discussions and insights.

## Citation

```bibtex
@misc{von-platen-etal-2022-diffusers,
  author = {Patrick von Platen and Suraj Patil and Anton Lozhkov and Pedro Cuenca and Nathan Lambert and Kashif Rasul and Mishig Davaadorj and Thomas Wolf},
  title = {Diffusers: State-of-the-art diffusion models},
  year = {2022},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/huggingface/diffusers}}
}
```
