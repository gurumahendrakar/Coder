from PIL import Image,ImageFilter
import os
from PIL import *
def image_croping():

##-----------------------------------------------------------------------------------------------------------------------------------------------

    #Image Information.......
    """
         x = x me kahase start karna hai uska width
         y = y  me kahase start karna hai
         z = x ko kahape khatam karna hai
         y = y k0 kahape khatam karna hai
        """
    image_path_  = Image.open(r"dog.jpg")
    print('Konsi Format ka hai',image_path_.format)
    print('Image Size',image_path_.size)
    print('Image width ',image_path_.width)
    print('Image Height',image_path_.height)

# -----------------------------------------------------------------------------------------------------------------------------------------------
                                      #Image Rotating...

    #image rotate arguments....

    # 1) fillcolor = 'white'
    # 2) expand =True # image rotate hone ke baad side ko black background bana deta hai

    rotate = image_path_.rotate(90,expand=True,fillcolor='white',)
    image_crop = image_path_.crop((0,400,1920,1600))

    #Image Resizeing.....

#-----------------------------------------------------------------------------------------------------------------------------------------------
                                                #Image Resizeing.....

    resize_image = image_path_.resize((40,40))
    resize_image.save('dogresize_image.png')
    resize_image.show()


#------------------------------------------------------------------------------------------------------------------------------------------------
                                          #Image Transforming.......

    #image transforming
    #TRANSPOSE
    #FLIP_LEFT_RIGHT
    #FLIP_TOP_BOTTOM
    # Image.ROTATE_90 Image.ROTATE_180 Image.ROTATE_270
    transform = image_path_.transpose(Image.ROTATE_180)


##-----------------------------------------------------------------------------------------------------------------------------------------------


image_croping()