import piexif
from PIL import Image

# exif_dict = piexif.load('C:/Users/matt/OneDrive/Pictures/2006-05 - Graduation Slide Show Pictures/Matt in A paper bag.jpg')
# －DateTimeOrginal; ID= 36867 －DateTimeDigitized; ID= 36868 

#exif_dict = piexif.load(r"C:\Users\matt\OneDrive\Pictures\2015-01-16\2014-01-10-Nickelodeon_Universe.jpg")
exif_dict = piexif.load(r"C:\Users\matt\OneDrive\Desktop\photo_scanner\DingleFritz-Accnt_3.jpg")

for ifd_name in exif_dict:
    print("\n{0} IFD:".format(ifd_name))
    for key in exif_dict[ifd_name]:
        try:
            print(key, exif_dict[ifd_name][key][:10])
        except:
            print(key, exif_dict[ifd_name][key])
