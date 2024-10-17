from diffusers import DiffusionPipeline

model = "runwayml/stable-diffusion-v1-5"
pipe = DiffusionPipeline.from_pretrained(model)

def generate_landscape(color):
    prompt = f"A beautiful landscape with a dominant color of {color}."
    images = pipe(prompt, num_inference_steps=20).images
    images[0].show()

while True:
    color = input("Enter a color for the landscape (e.g., blue, red, green):\n>>> ")
    
    generate_landscape(color) 

model = "runwayml/stable-diffusion-v1-5"
pipe = DiffusionPipeline.from_pretrained(model)

def generate_landscape(color):
    prompt = f"A beautiful landscape with a dominant color of {color}."
    images = pipe(prompt, num_inference_steps=20).images
    images[0].show()

while True:
    color = input("Enter a color for the landscape (e.g., blue, red, green):\n>>> ")
    
    generate_landscape(color)