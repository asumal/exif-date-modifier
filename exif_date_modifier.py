import os
import sys

from exif import Image
from datetime import datetime

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
    """
    Saves a file in a (date-specific) directory within the existing directory
    """
     
    output_path = os.path.join(output_directory, file_name)
    with open(output_path, 'wb') as new_image_file:
        new_image_file.write(my_image.get_file())


if __name__ == '__main__':
    all_args = sys.argv[1:]
    if (len(all_args) != 2):
        exit("need two arguments")
    
    directory = all_args[0]
    log(f"directory with files: {directory}")
    output_directory = create_output_directory(directory)
    log(f"output directory: {output_directory}")

    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            log(f"file_path: {f}")
            with open(f, 'rb') as image_file:
                my_image = Image(image_file)

                #do some work

                # save changes
                output_directory = create_output_directory(directory)
                save_image(output_directory, my_image, filename)
