import  contextlib


# class __call:
#
#     def __call__(self,*args):
#         print(*args)
#
# class contextlib2(__call):
#     def __init__(self,function):
#         self.open = open('texting.txt','r')
#
#     def __enter__(self):
#         print("Textwrapper_io object Was Created You Can (Write & Read)")
#         print()
#         return self.open
#
#     def __exit__(self, exc_type, exc_value, traceback):
#         print(" Error : {}\n"
#               " Error Message :{}\n"
#               " traceback (file Object) : {}".format(exc_type,exc_value,traceback))
#
#         self.open.close()
#         print('File Closed')
#
#
#         if exc_type==type(FileNotFoundError()):
#             return True
#
#         elif exc_type==type(EOFError):
#             return True #-> Error Nahi Dega return True likhna Compulsary nahi to koi effect nahi padega
#                                     # Error Dega
#
# @contextlib2
# def wrappingcontextlib2():
#     print("Hey Man I M Guru") # Jab Tum Function Ke Saath Wrapping Karte Ho Normal Class Jaisa Chalta Hai
#
#
#
# with contextlib2('Hey Bro ! Whats\' Doing Brother') as file:
#     raise FileNotFoundError
#
#
#
# print(wrappingcontextlib2('Hlo Brother'))




#-----------------------------------------contextmanager function---------------------------------------------

@contextlib.contextmanager
def contextmanagerr():
    try:
        open1 = open('texting.txt','w')
        yield open1
    except Exception as e:
        print('Error -------',e)

    else:
        print("Your Work is Completed.")




with contextmanagerr() as uou:
    print(uou.write('Hlo Brother')) # file.write(object,(write-string))-> return len(stringpassed)

