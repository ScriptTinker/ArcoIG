import torch
from diffusers import FluxPipeline
import os

class ImageGenerator:
    def __init__(self):
        self.pipe = None
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.token = os.getenv("HF_TOKEN")
        
    def load_model(self):
        if self.pipe is None:
            print("Caricamento modello...")
            self.pipe = FluxPipeline.from_pretrained(
                "black-forest-labs/FLUX.1-schnell",
                torch_dtype=torch.bfloat16
            )
            self.pipe.to(self.device)
            print("Modello caricato!")
    
    def generate(self, prompt, num_inference_steps=4, guidance_scale=0.0):
        if self.pipe is None:
            self.load_model()
        
        image = self.pipe(
            prompt,
            num_inference_steps=num_inference_steps,
            guidance_scale=guidance_scale
        ).images[0]
        
        return image

generator = ImageGenerator()