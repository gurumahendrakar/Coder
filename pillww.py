# from PIL import Image,ImageFilter
# import os
# from PIL import *
#
# # def image_croping():
# #
# # ##-----------------------------------------------------------------------------------------------------------------------------------------------
# #
# #     #Image Information.......
# #     """
# #          x = x me kahase start karna hai uska width
# #          y = y  me kahase start karna hai
# #          z = x ko kahape khatam karna hai
# #          y = y k0 kahape khatam karna hai
# #         """
# #     image_path_  = Image.open(r"allfiles/dog.jpg")
# #     print('Konsi Format ka hai',image_path_.format)
# #     print('Image Size',image_path_.size)
# #     print('Image width ',image_path_.width)
# #     print('Image Height',image_path_.height)
# #
# #
# #
# # # -----------------------------------------------------------------------------------------------------------------------------------------------
# #                                       #Image Rotating...
# #
# #     # image rotate arguments....
# #
# #     # 1) fillcolor = 'white'
# #     # 2) expand =True # image rotate hone ke baad side ko black background bana deta hai
# #
# #     rotate = image_path_.rotate(90,expand=True,fillcolor='white',)
# #     image_crop = image_path_.crop((500,0,image_path_.width,image_path_.height))
# #     image_crop.show()
# #
# #     # Image Resizeing.....
# #
# # #-----------------------------------------------------------------------------------------------------------------------------------------------
# #                                                 #Image Resizeing.....
# #
# #     # resize_image = image_path_.resize((40,40))
# #     # resize_image.save('dogresize_image.png')
# #     # resize_image.show()
# #
# #
# # #------------------------------------------------------------------------------------------------------------------------------------------------
# #                                           #Image Transforming.......
# #
# #     #image transforming
# #     #TRANSPOSE
# #     #FLIP_LEFT_RIGHT
# #     #FLIP_TOP_BOTTOM
# #     # Image.ROTATE_90 Image.ROTATE_180 Image.ROTATE_270
# #     transform = image_path_.transpose(Image.ROTATE_180)
# #
# #
# # ##-----------------------------------------------------------------------------------------------------------------------------------------------
# #
# #
# # image_croping()
# import os
# os.chdir('S:/pygame')
# image_ = Image.open(r'S:/pygame/player_sprites.png')
# print(f'total {image_.width} {image_.width//5}')
# print(f'total {image_.height} {image_.height//3}')
#
#
# #
# image_.crop((0,0,51*1,48)).show()
# image_.crop((51*1,0,51*2,48)).show()
# image_.crop((51*2,0,51*3,48)).show()
# image_.crop((51*3,0,51*4,48)).show()
# image_.crop((51*4,0,51*5,48)).show()
# =======
# def image_croping():
#
# ##-----------------------------------------------------------------------------------------------------------------------------------------------
#
#     #Image Information.......
#     """
#          x = x me kahase start karna hai uska width
#          y = y  me kahase start karna hai
#          z = x ko kahape khatam karna hai
#          y = y k0 kahape khatam karna hai
#         """
#     image_path_  = Image.open(r"dog.jpg")
#     print('Konsi Format ka hai',image_path_.format)
#     print('Image Size',image_path_.size)
#     print('Image width ',image_path_.width)
#     print('Image Height',image_path_.height)
#
# # -----------------------------------------------------------------------------------------------------------------------------------------------
#                                       #Image Rotating...
#
#     #image rotate arguments....
#
#     # 1) fillcolor = 'white'
#     # 2) expand =True # image rotate hone ke baad side ko black background bana deta hai
#
#     rotate = image_path_.rotate(90,expand=True,fillcolor='white',)
#     image_crop = image_path_.crop((0,400,1920,1600))
#
#     #Image Resizeing.....
#
# #-----------------------------------------------------------------------------------------------------------------------------------------------
#                                                 #Image Resizeing.....
#
#     resize_image = image_path_.resize((40,40))
#     resize_image.save('dogresize_image.png')
#     resize_image.show()
#
#
# #------------------------------------------------------------------------------------------------------------------------------------------------
#                                           #Image Transforming.......
#
#     #image transforming
#     #TRANSPOSE
#     #FLIP_LEFT_RIGHT
#     #FLIP_TOP_BOTTOM
#     # Image.ROTATE_90 Image.ROTATE_180 Image.ROTATE_270
#     transform = image_path_.transpose(Image.ROTATE_180)
#
#
# ##-----------------------------------------------------------------------------------------------------------------------------------------------
#
#
import os

from PIL import Image
os.chdir('S:/pygame')

x = Image.open('S:/pygame/player_sprites.png')
print('x',x.width//5, 'y',x.height//3)

o,p,plus,oo,ooo = 0,50,0,0,48
if __name__ == '__main__':

    for xx in range(3):
        for xxx in range(5):
            x.crop((o,oo,p,ooo)).resize((130,150)).save(str(plus)+'.png')
            o, p = p, p + 49
            plus+=1
        o,p = 0,50
        oo,ooo = ooo,ooo+ooo


