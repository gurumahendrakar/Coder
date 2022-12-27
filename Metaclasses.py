
#child class ne parent class ko inherite kiya

#parent class ke pass __new __ hai to __new__ se Object Banega


# parent ke paas __new__ nahi hai( __init__ and __call__ hai to __call__ se object banega)
     # __init__ me saare class_type ,(method,),attributes jayege
     # Is ki madad se __object__ create karenge __call__ ke andar __new__ ki Help__ se 


# parent class __new__  nahi  (__init__ or __call__ ) Hone Chahiye ye Dono Nahi Hai to Builtin Object me  __new__ method se Object Create Karega




class typemethod:
    name = 'Guru'
    def __init__(self,name,bases,cdict):
        self.name = name
        self.bases = bases
        self.cdict = cdict

    cls_intances = {}

    def __new__(self,class_name,inherited_classes,attributes):
<<<<<<< HEAD
        return type(class_name,inherited_classes,attributes)
=======
        pass
>>>>>>> a61a249b50f3ad60a15e2e96bd630d1606ad1418

    def __call__(cls,*args,**kwargs):


        if cls in typemethod.cls_intances :
            return "YOu Are Created More Objects"
        else:
            print(cls.cdict)
            typemethod.cls_intances[cls] = type(cls.name,cls.bases,cls.cdict)
            return type('Guru',(),{})


    def __add__(self,otherself):
        print("Entered")
        return self.name + otherself.name

class Mymethod(metaclass=typemethod):
    online = 'Online Classes'
    def __init__(self):

        self.name = "Syed Ali"
        self.sirname = "Chowdary"

    def __mro__(self):
        print("Cooled Brother")

    def __add__(self,otherself):
        print("Entered")
        return self.name + otherself.name

my = Mymethod

my2 = typemethod('Guru','Fuck','Tool')

print(my2)

