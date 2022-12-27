from typing import List,Tuple,Any,Dict,Union,Sequence,Optional,Set,Iterable,Generator,Callable

lst_ : List[List[Union[str,int]]]= [[2,'guru']]
tup : Tuple[Tuple[int,int]]
dct = Dict[str,int]
Sqnce = Sequence[Union[int,Any]]
optinal = Optional[Dict[str,int]]
iterablee = Iterable
Genratorrr = Generator

def fun(a : int ,b:int)-> None:
    print(a,b)

def fun2(list_:Callable[[int,int],int])-> Iterable:
    return list_


fun2(fun(1,2))