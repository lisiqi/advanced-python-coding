# Dunder methods are special methods in Python that start and end with double underscores (e.g., __init__, __str__, __len__).
# They are also known as magic methods.
# Dunder methods allow you to implement behavior for built-in operations or functions.  

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other): # called by + operator
        return Vector(self.x + other.x, self.y + other.y)   

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"   

    def __mul__(self, other): # called by * operator
        return Vector(self.x * other.x, self.y * other.y)   

v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)
print(v1 * v2)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __del__(self):
        print("Person object is being deleted")

    def __str__(self): # called by print()
        return f"Person(name={self.name}, age={self.age})"  

    def __repr__(self): # called by repr()
        return f"Person(name={self.name}, age={self.age})"

    def __len__(self):
        return len(self.name)

    def __call__(self): # called by calling the object like a function
        print(f"Hello, I am {self.name} and I am {self.age} years old.")


p = Person("John", 20)
print(p)
print(len(p))
p()