######## IMPORTS ########
# Local imports
import src.spotipy as spotipy
import src.image_gen_StableDiffusion as stable_diffusion
import src.image_gen_DALLE as dalle

# External imports
import argparse


######## MAIN ########

def main(args):
    ############### SPOTIPY ###############
    # Load the environment variables
    client_id, client_secret, playlist_id = spotipy.load_environment_variables()

    # Call the setup_spotify function to set up the Spotify client
    sp, playlist = spotipy.setup_spotify(client_id, client_secret, playlist_id)

    # Get the playlist
    df = spotipy.get_tracks_and_artists(playlist, sp)

    # Create a list of the songs and the artists [format: song_name - artist_name]
    songs = spotipy.get_song_artist_list(df)

    ############### IMAGE GENERATION (Using Stable Diffusion) ###############
    # Load the model
    pipe = stable_diffusion.load_model()

    # Generate the image
    image = stable_diffusion.generate_image(songs, pipe)

    # Save the image to output folder
    stable_diffusion.save_image(image)

    ############### IMAGE GENERATION (Using DALLE) [Comment out the ### to use DALL·E (requires an OpenAI API access token (see readme.md))] ###############
    # Load the environment variables
    ###openai_key = dalle.load_environment_variables()
    
    # Enter OpenAI API key
    ###dalle.setup_openai(openai_key)
    
    # Generate the image
    ###image_url = dalle.generate_image(songs)

    # Save the image to output folder
    ###dalle.save_image(image_url)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='This script takes song and artist names from selected Spotify playlists as input and uses these to generate images that resembles the content of the playlist. Type --help to see all the possible arguments.')
    
    # Arguments for stable diffusion
    parser.add_argument('--model_id', type=str, default="runwayml/stable-diffusion-v1-5", help='The model id for the Stable Diffusion model. Default: runwayml/stable-diffusion-v1-5. You can change this to any model id from the HuggingFace model hub (https://huggingface.co/models?pipeline_tag=text-to-image&sort=downloads).')
    parser.add_argument('--neg_prompt', type=str, default="text characters", help='The negative prompt for the Stable Diffusion model. Default: text characters. This is the text that the model should avoid when generating the image. You can change this to any text you want the model to avoid.')
    parser.add_argument('--width', type=int, default=512, help='The width of the image. Default: 512. You can change this to any width you want. We recommend using a square image.')
    parser.add_argument('--height', type=int, default=512, help='The height of the image. Default: 512. You can change this to any height you want. We recommend using a square image.')

    # Arguments for DALL·E
    parser.add_argument('--openai_api_key', type=str, default="", help='The OpenAI API key for the DALL·E model. Default: "". You can change this to your own OpenAI API key.')
    parser.add_argument('--n', type=int, default=1, help='The number of images to generate. Default: 1. You can change this to any number you want.')
    parser.add_argument('--size', type=str, default="512x512", help='The size of the image. Default: 512x512. You can change this to any size you want. We recommend using a square image e.g. "256x256", "512x512", "1024x1024".')

    args = parser.parse_args()
    main(args)