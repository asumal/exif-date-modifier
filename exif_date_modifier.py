import os
import sys

from exif import Image, DATETIME_STR_FORMAT
from datetime import datetime


DATE_KEYS = ['datetime', 'datetime_digitized', 'datetime_original']


def log(message):
    print(f"LOG: {message}") 


def create_output_directory(working_directory):
    t = datetime.now()
    log(t)
    directory_name = t.strftime("%m-%d-%Y_%H:%M:%S")
    output_path = os.path.join(working_directory, 'output', directory_name)
    
    isExist = os.path.exists(output_path)
    if not isExist:
        os.makedirs(output_path)

    return output_path


def save_image(output_directory, my_image, file_name):     
    output_path = os.path.join(output_directory, file_name)
    with open(output_path, 'wb') as new_image_file:
        new_image_file.write(my_image.get_file())


if __name__ == '__main__':
    all_args = sys.argv[1:]
    if (len(all_args) != 2):
        exit("need two arguments")
    
    directory = all_args[0]
    log(f"directory with files: {directory}")

    new_date = datetime.strptime(all_args[1], "%Y-%m-%d %H:%M:%S")
    log(f"new date: {new_date}")

    output_directory = create_output_directory(directory)
    log(f"output directory: {output_directory}")

    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            log(f"file_path: {f}")
            with open(f, 'rb') as image_file:
                my_image = Image(image_file)

                #update date exif metadata
                for date_key in DATE_KEYS:
                    date_value = my_image.get(date_key);
                    log(f"old date_value '{date_value}' for key '{date_key}'")
                    
                    my_image[date_key] = new_date.strftime(DATETIME_STR_FORMAT) 

                # save changes to new location
                save_image(output_directory, my_image, filename)
