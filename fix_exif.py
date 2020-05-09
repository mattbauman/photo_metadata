from pathlib import Path
import sys
import os
import json
import time
import piexif
from PIL import Image

def fix_efix(input_image_path):
    input_image_path = str(input_image_path)
    try:
        exif_dict = piexif.load(input_image_path)
    except:
        pass
    
    try:
        DateTimeOriginal = exif_dict['Exif'][36867]
    except:
        DateTimeOriginal = ''
    try:
        DateTimeDigitized = exif_dict['Exif'][36868]
    except:
        DateTimeDigitized = ''

#find json
    try:
        windows_photo_path_json = input_image_path
        windows_photo_path_json = windows_photo_path_json.replace("-edited.", ".")
        windows_photo_path_json = windows_photo_path_json.replace("(1)", "")
        windows_photo_path_json = windows_photo_path_json.replace("(2)", "")
        windows_photo_path_json = windows_photo_path_json.replace("(3)", "")
        windows_photo_path_json = windows_photo_path_json+".json"
        google_json = json.loads(open(windows_photo_path_json, 'r').read())
        google_photoTakenTime = time.localtime(int(google_json['photoTakenTime']['timestamp']))
        google_photoTakenTime = time.strftime("%Y:%m:%d %H:%M:%S", google_photoTakenTime)
        google_photoTakenTime = str.encode(google_photoTakenTime)
    except:
        google_photoTakenTime = ''

    if str(DateTimeOriginal) == '' and str(google_photoTakenTime) != '':
        update_flg = True
    else:
        update_flg = False
#write new file
    if update_flg:
        #set new values
        exif_dict['Exif'][36867] = google_photoTakenTime
        exif_dict['Exif'][36868] = google_photoTakenTime
        #build export
        output_image_path = input_image_path.replace("C:","D:")
        output_image_directory = output_image_path.split('\\')
        output_image_directory = output_image_directory[0:len(output_image_directory)-1]
        output_image_directory = '\\'.join(output_image_directory)
        try:    
            os.makedirs(output_image_directory)
        except:
            pass
        im = Image.open(input_image_path)
        exif_bytes = piexif.dump(exif_dict)
        im.save(output_image_path, exif=exif_bytes)

    print_record = [str(input_image_path), str(DateTimeOriginal), str(DateTimeDigitized), str(google_photoTakenTime), str(update_flg)]
    out.write('|'.join(print_record))
    out.write('\n')

#        －DateTimeOrginal; ID= 36867 －DateTimeDigitized; ID= 36868 
image_path = "C:/Users/matt/OneDrive/Pictures"
image_list = list(Path(image_path).rglob("*.[jJ][pP][eE][gG]"))
image_list = image_list + list(Path(image_path).rglob("*.[jJ][pP][gG]"))
out = open("out.txt",'w')
out.write('input_image_path|DateTimeOriginal|DateTimeDigitized|google_photoTakenTime|update_flg')
out.write('\n')

for image_path in image_list:
    try:
        fix_efix(image_path)
    except:
        print("main function call fail")
