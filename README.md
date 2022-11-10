# apod_desktop

Program that takes a random Astronomy Picture of the Day (https://apod.nasa.gov/apod/astropix.html) image and sets it as your desktop background.

In the config file:

1. Generate your NASA API key (api_key = '') at https://api.nasa.gov/

2. Define where you will save the image (image_file = '') for the system to access, as well the location of an HTML file (html_file = '') that will open to the original webpage of that APOD

3. Define the command to place the setting the desktop background image (destination = ''), e.g, " '/usr/bin/gsettings set org.gnome.desktop.background picture-uri' ". The program will append the file location to the command.

Run <apod_desktop_main.py>
