# Solution to SDA test 01

## Getting started

Run the following commands in order to generate the output PDF file.
Probably the next commands won't work in Windows.

```bash
# Install python 3.
# At the moment this was written, this commands installs python 3.8.10
sudo apt-get update
sudo apt-get install python3

# Install venv
sudo apt-get install python3-dev python3-venv

# Create the .venv directory.
python3 -m venv .venv/

# Activate the python venv environment
source ./.venv/bin/activate

# Now you should see a '(.venv)' in your terminal
# Just in case, upgrade pip
pip install --upgrade pip

# Install the proyect python packages
pip install -r requirements.txt

# Run it
python __init__.py
```

That will create a file called out.pdf in the root directory of this project.
