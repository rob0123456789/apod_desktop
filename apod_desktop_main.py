import apod_desktop as ap



def main():

    key, im_file, url_file, destination = ap.fetch_config()

    day = ap.today()

    url, url_Date = ap.image_get(day, key)

    ap.save_image(url, im_file)

    ap. write_desktop(im_file, destination)

    ap.write_HTML(url_Date, url_file)

    return


if __name__ == '__main__':
    main()