import requests
import random
from datetime import datetime, timedelta
import shutil
import os
import apod_config as apc



# Retern the complete set of configuration variables

def connected_to_internet(url='https://apod.nasa.gov/apod/astropix.html', timeout=5):
    try:
        _ = requests.head(url, timeout=timeout)
        return True
    except requests.ConnectionError:
        print("No internet connection available.")
    return False

def fetch_config():

    return apc.api_key, apc.image_file, apc.html_file, apc.desktop_command

#Set the date range between Jan 1 2015 and today (image quality is generally better after Jan 1 2015)
def today():

    today = datetime.today()
    firstDay = datetime.strptime('2015-01-01', '%Y-%m-%d')
    day = today - firstDay

    #pick a random date
    n = random.randrange(0, day.days)
    date = today - timedelta(days=n)

    return date



# Get the image url  ensuring it is an image
def image_get(date, key):
    url = ''

    # Only work with APODs that include an image. JPG is their standard format

    while url.find('jpg') == -1:

        #Define the formats for the APOD API and the APOD url for the desktop HTML files
        apod_date = date.strftime('%Y-%m-%d')
        url_date = date.strftime('%y%m%d')

        #fetch the response using the APOD API including explanations
        api_url = 'https://api.nasa.gov/planetary/apod?api_key=' + key + '&date=' + apod_date
        response = requests.get(api_url)
        json_r = response.json()
        url = json_r['url']
        print(json_r)
    
    return url, url_date



# Save image and set as desktop
def save_image(url, image_file):

    response = requests.get(url, stream=True)
    
    with open(image_file, 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    
    out_file.close()
    
    del response

    return


def write_desktop(image_file, destination):

    argument = destination + ' ' + image_file
    os.system(argument)

    return 

# Write the url to an html file to open the webpage from the desktop
def write_HTML(date, html_file):

    html = """
    <html>
        <head>
            <meta http-equiv="refresh" content="0; url=https://apod.nasa.gov/apod/ap""" + date + """.html" />
        </head>
        <body> </body>
    </html>
    """

    with open(html_file, "w") as file:

        file.write(html)

    return