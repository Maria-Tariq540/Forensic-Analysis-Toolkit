import exifread

def get_exif_data(image_path):

    exif_data = {}

    with open(image_path, "rb") as image:

        tags = exifread.process_file(image)

        for tag in tags.keys():
            exif_data[tag] = str(tags[tag])

    return exif_data