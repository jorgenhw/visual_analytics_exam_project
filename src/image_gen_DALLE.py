import openai
import requests

# enter openAI API key
def setup_openai():
    openai.api_key = input("Enter your OpenAI API key: ")

def genrate_image(songs,
                  n=1,
                  size="512x512"):
    response = openai.Image.create(
        prompt= f'Generate an artistic representation of a playlist using song titles as the theme. Imagine an abstract painting that captures the essence of the songs. Incorporate vibrant colors and dynamic shapes to evoke the emotions and moods conveyed by the following list of songs: {songs}. The artwork should be visually captivating, with fluid brushstrokes and a sense of movement.',
        n=n, # number of images to generate
        size=size # alternative image sizes: "256x256", "512x512", "1024x1024"
        )
    image_url = response['data'][0]['url'] # get the image url
    return image_url

# Download the image locally
def save_image(image_url):
    image_data = requests.get(image_url).content
    with open('DALLE_image.png', 'wb') as file:
        file.write(image_data)