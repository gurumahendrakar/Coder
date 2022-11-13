
# Easy Understanding Decorators For Begginners 

def name_spliter(decorator_1):
    def circus():
        return decorator_1().split(" ")

    return circus


def Word_capitalize(decorator_2):
    def Board_():
        return decorator_2()
    return Board_


@name_spliter
@Word_capitalize
def decorator_1():
    Name = input("Enter Name : ")
    Sirname = input('Enter Sirname : ')
    return Name + Sirname

print(decorator_1())

print("Congratus Mission Completed ")



#@wraps with decorators work

from functools import wraps
def yellow(toool):
    @wraps(toool)
    def yellow2():
        """Guru Mahendrakar Im Yellow 2"""
        print(toool.__doc__)
    return yellow2
@yellow
def tool():
    """Guru Mahendrakar Im Tool """
    return "Guru Ji Mahendrakar"

print(tool.__name__) # tool ayega @wraps hai bolke @wraps nahi hoga to return kiya so name return hoga