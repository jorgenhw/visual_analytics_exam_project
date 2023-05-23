<!-- PROJECT LOGO -->
<br />
<p align="center">
  <h1 align="center">Cultural Datascience 2023</h1> 
  <h2 align="center">Final project</h2> 
  <h3 align="center">Visual Analytics</h3> 


  <p align="center">
    Jørgen Højlund Wibe<br>
    Student number: 201807750
  </p>
</p>


<!-- ABOUT THE PROJECT -->
## About the project
This project enables you to change your Spotify playlist cover photos with images that artistically resembles the content of the playlist. This is achieved through the use of state-of-the-art text-to-image generaters. The inputs to the image generator are the song titles and belonging artists (obtained via [Spotify's API](https://developer.spotify.com/documentation/web-api)). The output is a creative and artsy visual representation.

To show how it works, two sample photos are included in the ```samples``` folder. These are images generated using this method on 1) a playlist containing rock music and 2) a playlist containing classical music. These serves as an example of how the model interprets playlists visually. URI's to the playlists are located in ```sample_playlists.txt```.

<!-- USAGE -->
## Usage

To use or reproduce the results you need to adopt the following steps.

**NOTE:** There may be slight variations depending on the terminal and operating system you use. The following example is designed to work using the Visual Studio Code version 1.77.3 (Universal). The terminal code should therefore work using a unix-based bash. The avoid potential package conflicts, the ```setup.sh``` bash files contains the steps necesarry to create a virtual environment, install libraries and run the project.

1. Get a free Spotify API Key
2. Get a Spotify playlist ID
3. Clone repository
4. Update the ```.env``` file
5. Run ```setup.sh```

### Get Spotify API keys
In order to get the required Spotify API keys, you'll need to create a Spotify application through their Developer Dashboard. Here's a step-by-step guide to help you get started:

1. Login/register with your Spotify credentials at the [**Spotify Developer Dashboard**](https://developer.spotify.com/).
2. Once you're logged in, navigate to the Dashboard and click on the **"Create App"** button.
3. **Fill in** the application details and create it.
4. Obtain the **client ID** and **client secret**: On the application settings page, you'll find your client_id and client_secret. These are unique identifiers for your application and are necessary for authenticating your requests to the Spotify API. Store them securely.

### Get a Spotify playlist URI
To obtain a Spotify Playlist URI, open your Spotify Desktop app and navigate to a playlist. You can copy the Spotify URI by
1. Clicking on the three dots opening the playlist settings
2. Hover over **Share**
3. Hold **Alt** (on Mac) or **Ctrl** (on Windows)
4. Click on: '**Copy Spotify URI**'.

The URI looks like this: *"spotify:playlist:2e3scy56lPjABWt1DHTJvH"*

### Clone repository

Clone repository using the following lines in the unix-based bash:

```bash
git clone https://github.com/jorgenhw/visual_analytics_exam_project.git
cd visual_analytics_exam_project
```

### Update the ```.env``` file
Open the ```.env``` file and insert your ```client_id```, ```client_secret``` and ```playlist URI``` into the specified fields. Save file. These are now global environment variables which the script can read when you run it.

### Run ```setup.sh```

To replicate the results, I have included a bash script that automatically 

1. Creates a virtual environment for the project
2. Activates the virtual environment
3. Installs the correct versions of the packages required
4. Runs the script
5. Deactivates the virtual environment

Run the code below in your bash terminal:

```bash
bash setup.sh
```

Once you've started the script you'll be asked to enter your Spotify API keys and a playlist URI. Enter these in the command line.

### Changing arguments via ```argparse```
To provide more flexibility and enable the user to change the parameters of the script from the command line, we have implemented argparse in our script. This means that by running the script with specific command line arguments, you can modify parameters such as the batch size, the number of epochs to train the model, and the learning rate.

To see all the available arguments, simply run the command:

```bash
python main.py --help
```

## Inspecting results

The generated image will be located in the ```output``` folder. Here one can inspect the results.

<!-- REPOSITORY STRUCTURE -->
## Repository structure

This repository has the following structure:
```
│   main.py
│   README.md
│   requirements.txt
│   setup.sh
│
├───data
│       empty folder [put your data here]
│
├───out
│       classification_report.txt
│       training_and_validation_plots.png
│
└──src
        data_wrangling.py
        classifier.py
        evaluation.py
```


<!-- DATA -->

## Data


<!-- RESULTS -->

## Remarks on findings
Overall, this project demonstrates the use of a pretrained CNN for image classification and the effectiveness of data augmentation and data generators in improving training efficiency. However, it should be clearly stated that this project project is for educational purposes only. Nothing has been done to find the optimal hyper parameters such as batch size, number of epochs, or learning rate.