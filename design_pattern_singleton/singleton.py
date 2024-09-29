from abc import ABCMeta, abstractmethod

class IPerson(metaclass=ABCMeta):
    @abstractmethod
    def print_data():
        """Implement in derived class"""
        
class PersonSingleton(IPerson):
    __instance = None
    
    @staticmethod
    def get_instance():
        if PersonSingleton.__instance == None:
            PersonSingleton("Default Name", 0)
        return PersonSingleton.__instance
    
    def __init__(self, name, age):
        if PersonSingleton.__instance != None:
            raise Exception("Singleton cannot be instantiated more than once")
        else:
            self.name = name
            self.age = age
            PersonSingleton.__instance = self
        
    @staticmethod
    def print_data():
        print(f"Name: {PersonSingleton.__instance.name}, Age: {PersonSingleton.__instance.age}")    
        
p1 = PersonSingleton("John", 30)
print(p1)
p1.print_data()

# p2 = PersonSingleton("Bob", 30) # Exception: Singleton cannot be instantiated more than once
# p2.print_data()
p2 = PersonSingleton.get_instance()
p2.print_data()