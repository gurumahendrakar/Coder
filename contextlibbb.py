import  contextlib


class __call:

    def __call__(self,*args):
        print(*args)

class contextlib2(__call):
    def __init__(self,function):
        self.open = open('texting.txt','r')

    def __enter__(self):
        print("Textwrapper_io object Was Created You Can (Write & Read)")
        return self.open

    def __exit__(self, exc_type, exc_value, traceback):
        print(" Error : {}\n"
              " Error Message :{}\n"
              " traceback (file Object) : {}".format(exc_type,exc_value,traceback))

        if exc_type==type(FileNotFoundError()):
            return True

        elif exc_type==type(EOFError):
            return True #-> Error Nahi Dega return True likhna Compulsary nahi to koi effect nahi padega
                                    # Error Dega

# @contextlib2
# def wrappingcontextlib2():
#     print("Hey Man I M Guru") # Jab Tum Function Ke Saath Wrapping Karte Ho Normal Class Jaisa Chalta Hai
#
#
#
with contextlib2('Hey Bro ! Whats\' Doing Brother') as file:
    file.write('Hey I am Guru')
#
#
#
# print(wrappingcontextlib2('Hlo Brother'))




#-----------------------------------------contextmanager function---------------------------------------------

# @contextlib.contextmanager
# def contextmanagerr():
#     # Pehle Yaha Ayega yield me open() ka object lega.... And jaha osko call kiya oska work complete karega else me jayega
#     try:
#         print('Creating Object Creating...')
#         open1 = open('texting.txt','r+')
#         yield open1
#     except FileNotFoundError as e:
#         raise FileNotFoundError('Your File Not in Directory')

#     else:
#         print('Closeing File...')
#         open1.close()



# a = contextmanagerr()

# with a as uou:
#     uou.write('Hlo B rther') # file.write(object,(write-string))-> return len(stringpassed)
#     print('Writing Completed')
# print(uou.closed)