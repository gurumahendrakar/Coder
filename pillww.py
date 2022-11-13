from PIL import Image,ImageFilter
import os
def image_croping():
    """
         Startwidth = Kahase Start Karna width me
        Startheingt = kahse Start Karna Hai Height Me

         width  = Kahatak Crop Karna Hai Width me
         Height = Kahatak Crop Karna Hai Height me
        """
    image_path_  = Image.open(r"C:\Users\mahen\bitepy\allfiles\io.jpg")
    rotate = image_path_.rotate(45)
    image_crop = image_path_.crop((300,300,1220,600))

    #image_path_crop(Startwidth,StartHeight,Width,height)

    image_crop.show()


a = Image.open(r"C:\Users\mahen\bitepy\allfiles\io.jpg")
ImageFilter.BLUR()
a.show()