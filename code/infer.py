from huggingface_hub.repocard import RepoCard
from diffusers import DiffusionPipeline
import torch
from PIL import Image, ImageDraw, ImageFont
import safetensors
from safetensors.torch import load_file, save_file

base_model_id = "/your_path/stable-diffusion-xl-base-1.0/stable-diffusion-xl-base-1.0"
lora_path = "/path_to_lora/pytorch_lora_weights.safetensors"
output_path = "/your_output_path"
prompt = "your prompt, see example below"
# prompt = "a woman walking a dog in w@z flat cartoon illustration style"

seed = 77

pipe = DiffusionPipeline.from_pretrained(base_model_id, torch_dtype=torch.float16)
pipe = pipe.to("cuda:0")

lora = safetensors.torch.load_file(lora_path)

pipe.load_lora_weights(lora)

generator = torch.Generator(device="cuda").manual_seed(seed)

image = pipe(prompt, 
            num_inference_steps=25, 
            generator=generator
            ).images[0]

image.save(output_path)