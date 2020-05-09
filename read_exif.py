import piexif
from PIL import Image

input_image = r"C:\Users\matt\OneDrive\Desktop\photo_scanner\DingleFritz-Accnt_3.jpg"
exif_dict = piexif.load(input_image)

for ifd_name in exif_dict:
    print("\n{0} IFD:".format(ifd_name))
    for key in exif_dict[ifd_name]:
        try:
            print(key, exif_dict[ifd_name][key][:10])
        except:
            print(key, exif_dict[ifd_name][key])
