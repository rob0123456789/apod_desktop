# apod_desktop

Program that takes a random Astronomy Picture of the Day (https://apod.nasa.gov/apod/astropix.html) image and sets it as your desktop background.

1. Generate your NASA API key at https://api.nasa.gov/ and place it in the config.py file

2. Define where you will save the image for the system to access, as well the location of an HTML file that will open to the original webpage of that APOD

3. Define the command to place the setting the deaktop background image, e.g, " '/usr/bin/gsettings set org.gnome.desktop.background picture-uri' ". The program will append the file location to the command.

Run <apod_desktop_main.py>
