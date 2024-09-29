def myfunction(myparameter: int):
    print(myparameter)


myfunction(1)  # prints 1
myfunction("Hello")  # prints Hello # no error


def myfunction2(myparameter: int) -> int:
    return myparameter + 1


print(myfunction2(1))  # prints 2


def otherfunction(otherparameter: str):
    print(otherparameter)


otherfunction(myfunction2(20))  # prints 21


print(myfunction2("Hello"))  # TypeError: can only concatenate str (not "int") to str
