class Person:
    def __init__(self, name, age):
        self.__name = name # private attribute
        self.__age = age # private attribute    
    
    @property # getter
    def Name(self):
        return self.__name
    
    @Name.setter # setter
    def Name(self, value):
        self.__name = value
    
    @staticmethod # static method: a method that is bound to the class, not the instance
    def mymethod(): # no need to use self
        print("Hello")

Person.mymethod()
    
p1 = Person("John", 20)
print(p1.Name)
p1.Name = "Jane"
print(p1.Name)
    
    

    # def __str__(self):
    #     return f"Person(name={self.name}, age={self.age})"

