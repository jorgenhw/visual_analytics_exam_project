from diffusers import DiffusionPipeline
import torch
import os

# Function to desired model
def load_model(model_id="runwayml/stable-diffusion-v1-5"):
    model_id = model_id
    pipe = DiffusionPipeline.from_pretrained(model_id,
        custom_pipeline="lpw_stable_diffusion", # allows us to process more than 77 tokens.
        torch_dtype=torch.float32
        )
    pipe.safety_checker = lambda images, clip_input: (images, False) # disables the safety check (as it retuned too many false positives)
    return pipe

# Function to generate image
def generate_image(songs, pipe,
                   neg_prompt="text characters",
                   width=512,
                   height=512):
    prompt = f"Generate an artistic representation of a playlist using song titles as the theme. Imagine an abstract painting that captures the essence of the songs. Incorporate vibrant colors and dynamic shapes to evoke the emotions and moods conveyed by the following list of songs: {songs}. The artwork should be visually captivating, with fluid brushstrokes and a sense of movement."
    neg_prompt = neg_prompt, # type the things you want to avoid in the image
    image = pipe.text2img(prompt,
                          negative_prompt = neg_prompt, 
                          width=width,
                          height=height,
                          max_embeddings_multiples=5).images[0]
    return image

# Function to save image
def save_image(image):
    image.save(os.path.join("output","StableDiffusion_image.png")) # Save the image in the 'output' directory




