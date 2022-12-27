import  contextlib
<<<<<<< HEAD
import io


class __call:

    def __call__(self,*args):
        print(*args)

class contextlib2():
    def __init__(self,function):
        self.open = open(function,'r')

    def __enter__(self):
        print("Textwrapper_io object Was Created You Can (Write & Read)")
        return self.open

    def __exit__(self, exc_type, exc_value, traceback):
        print(" Error : {}\n"
              " Error Message :{}\n"
              " traceback (file Object) : {}".format(exc_type,exc_value,traceback))

        if exc_type== type(io.UnsupportedOperation()):
            class readableChoice(Exception):
                def __init__(self,messege):
                    pass

            raise readableChoice('ye reading object hai isme aap write nahi kar sakte')

=======


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
>>>>>>> a61a249b50f3ad60a15e2e96bd630d1606ad1418
# @contextlib2
# def wrappingcontextlib2():
#     print("Hey Man I M Guru") # Jab Tum Function Ke Saath Wrapping Karte Ho Normal Class Jaisa Chalta Hai
#
#
#
<<<<<<< HEAD
with contextlib2('texting.txt') as file:
    file.write('Hey I am Guru')
=======
# with contextlib2('Hey Bro ! Whats\' Doing Brother') as file:
#     raise FileNotFoundError
>>>>>>> a61a249b50f3ad60a15e2e96bd630d1606ad1418
#
#
#
# print(wrappingcontextlib2('Hlo Brother'))




#-----------------------------------------contextmanager function---------------------------------------------

<<<<<<< HEAD
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
=======
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

>>>>>>> a61a249b50f3ad60a15e2e96bd630d1606ad1418
