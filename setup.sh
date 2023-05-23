# install requirements.txt for project
# Usage: source setup.sh

# create virtual environment
python3 -m venv playlist_image_generation_venv

# activate virtual environment
source ./playlist_image_generation_venv/bin/activate

# Install requirements
python3 -m pip install --upgrade pip # upgrade pip
pip3 install -r requirements.txt

# run the code
python3 main.py

# Extra: Type ```python3 main.py --help``` to see the help message for the adjustable parameters

# Deactivate virtual environment
deactivate