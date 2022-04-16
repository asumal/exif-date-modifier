# exif-date-modifier
A python script to modify the date EXIF fields of images in a particular directory. A new file is created in an `output` directory, leaving the original file unchanged

# usage
The script takes two parameters
1. `directory-path` the path to the directory of images to update
2. `date` the date to change the EXIF fields to. The format is `%Y-%m-%d %H:%M:%S`

## example
```
python exif_date_modifier.py `wedding-photos` `2022-01-02 3:44:34`
```
