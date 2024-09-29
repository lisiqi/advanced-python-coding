# Advanced Python Coding

Part of the content is based on the Youtube channel @NeuralNine 

Python depencies are managed with `poetry` in this repository. To install the dependencies, run the following command:

```sh
poetry install
```   

## Decorators
A decorator in Python is a design pattern that allows you to modify the behavior of a function or method without changing its actual code. Decorators are typically used to add functionality to existing functions in a clean and readable way.

### Benefits of Decorators:

1. **Code Reusability**: Decorators allow you to reuse common functionality across multiple functions without duplicating code.

2. **Separation of Concerns**: They help separate the core logic of a function from auxiliary concerns like logging, access control, or timing.

3. **Readability**: Decorators can make your code more readable by clearly indicating that a function has been modified or enhanced in some way.

4. **Maintainability**: By keeping the additional functionality separate, decorators make it easier to maintain and update your code.

### Example:

Here's a simple example to illustrate the use of a decorator for timing:

```python:decorator/2_timing.py
import time

def timed(function):
    def wrapper(*args, **kwargs):
        before = time.time()
        value = function(*args, **kwargs)
        after = time.time()
        fname = function.__name__
        print(f"{fname} took {after - before} seconds to execute!")
        return value
    return wrapper

@timed
def add(x, y):
    time.sleep(2)
    return x + y

print(add(1, 2))
```

#### Explanation:

1. **Decorator Function**: `timed` is a decorator function that takes another function as an argument and returns a new function (`wrapper`) that adds timing functionality.

2. **Wrapper Function**: The `wrapper` function records the time before and after calling the original function, calculates the elapsed time, and prints it.

3. **Applying the Decorator**: The `@timed` syntax is a shorthand for applying the `timed` decorator to the `add` function. It is equivalent to writing `add = timed(add)`.

4. **Enhanced Function**: When you call `add(1, 2)`, it actually calls the `wrapper` function, which times the execution of the original `add` function and prints the elapsed time.

#### Benefits Illustrated:

- **Code Reusability**: The timing functionality can be reused with any function by simply applying the `@timed` decorator.
- **Separation of Concerns**: The timing logic is separated from the core logic of the `add` function, making the code cleaner and easier to maintain.
- **Readability**: The `@timed` decorator clearly indicates that the `add` function has been enhanced with timing functionality.
- **Maintainability**: If you need to update the timing logic, you can do so in one place (the `timed` decorator) without modifying the `add` function or any other function that uses the decorator.

#### Output:

```
add took 2.0001230239868164 seconds to execute!
3
```

In this example, the decorator adds timing functionality to the `add` function, demonstrating how you can enhance or modify the behavior of functions in a clean and reusable way.


## Generators
A generator in Python is a special type of iterator that allows you to iterate over a sequence of values without creating the entire sequence in memory at once. This is particularly useful for handling large datasets or streams of data where it would be inefficient or impractical to store the entire sequence in memory.

### Benefits of Generators:

1. **Memory Efficiency**: Generators produce items one at a time and only when required, which means they use less memory compared to lists or other collections that store all items at once.

2. **Lazy Evaluation**: Generators compute values on the fly and yield them as needed, which can lead to performance improvements, especially when dealing with large datasets.

3. **Infinite Sequences**: Generators can represent infinite sequences, such as the Fibonacci sequence, without running out of memory.

4. **Improved Performance**: Since generators yield items one at a time, they can start producing results immediately and continue to do so as needed, which can lead to faster initial response times.

### Example:

Here's a simple example to illustrate the benefits of using a generator:

```python
def mygenerator(n):
    for x in range(n):
        yield x**3

values = mygenerator(9000000)

print(next(values))  # Output: 0
print(next(values))  # Output: 1
print(next(values))  # Output: 8
```

In this example, `mygenerator` yields the cube of each number from 0 to `n-1`. If `n` is very large (e.g., 9,000,000), using a generator is much more memory-efficient than creating a list of all these values.

### Comparison with List:

If you were to use a list instead of a generator, it would look like this:

```python
def mylist(n):
    return [x**3 for x in range(n)]

values = mylist(9000000)

print(values[0])  # Output: 0
print(values[1])  # Output: 1
print(values[2])  # Output: 8
```

This approach would require storing all 9,000,000 cubed values in memory at once, which could be very memory-intensive and slow.

In summary, generators provide a powerful and efficient way to handle large sequences of data by generating values on the fly and using memory only as needed.

## Argument Parsing

Argument parsing is the process of extracting information from command-line arguments and options. It allows you to create scripts that can be run from the terminal or command prompt with various inputs and configurations. Python provides several libraries for argument parsing, including `argparse`, `getopt`, and `optparse`.

### Benefits of Argument Parsing:

1. **Flexibility**: It allows you to define the structure of command-line arguments and options in a flexible and customizable way.

2. **Readability**: It makes your script more user-friendly and easier to understand by allowing users to specify inputs and configurations without having to read and understand the script's code.

3. **Automation**: It allows you to create scripts that can be automated and integrated into larger workflows, such as build processes or deployment pipelines.

4. **Portability**: It makes your script more portable, as it can be run on different systems with different configurations without requiring changes to the script itself.

### Example:

A simple example to illustrate the use of `argparse`: [1_argparse.py](argument_parsing/1_argparse.py)

A simple example to illustrate the use of `getopt`: [2_getopt.py](argument_parsing/2_getopt.py)

## Encapsulation
Encapsulation in Python is a fundamental concept in object-oriented programming that restricts direct access to some of an object's components, which can prevent the accidental modification of data. It is achieved using private attributes and methods, and providing public methods to access and modify them.

### Example

```python:encapsulation/encapsulation.py
class Person:
    def __init__(self, name, age):
        self.__name = name  # private attribute
        self.__age = age    # private attribute    
    
    @property  # getter
    def Name(self):
        return self.__name
    
    @Name.setter  # setter
    def Name(self, value):
        self.__name = value
    
    @staticmethod  # static method: a method that is bound to the class, not the instance
    def mymethod():  # no need to use self
        print("Hello")

Person.mymethod()  # Calling static method directly from the class
    
p1 = Person("John", 20)
print(p1.Name)  # Accessing private attribute via getter
p1.Name = "Jane"  # Modifying private attribute via setter
print(p1.Name)  # Accessing modified private attribute via getter
```

**Key Points:**
- **Private Attributes**: Use double underscores to make attributes private.
- **Getter and Setter**: Use `@property` and `@<property>.setter` to control access and modification of private attributes.
- **Static Method**: Use `@staticmethod` for methods that do not need access to instance or class attributes.

Encapsulation helps in maintaining the integrity of the data by providing controlled access and modification mechanisms.

## Type Hinting

Type hinting in Python is a feature that allows you to specify the expected type of an argument, return value, or attribute in a variable or function. It helps with code readability, maintainability, and can also be used by IDEs and static analysis tools like mypy to provide better error checking and suggestions. However, Python does not enforce type hints at runtime, meaning that type hints are primarily for documentation and tooling purposes.

### Benefits of Type Hinting

1. **Readability**: It makes the code more readable by clearly indicating the expected types of variables and parameters.

2. **Error Detection**: It can help detect type-related errors at an early stage, such as passing the wrong type of argument to a function.

3. **IDE Support**: IDEs can provide better code completion, type checking, and error detection based on the type hints.

4. **Static Analysis**: Static analysis tools can use type hints to perform more accurate analysis and provide more useful suggestions for code improvements.

### Example
Here's a breakdown of my [example code](type_hinting/type_hinting.py) with explanations:

```python:type_hinting/type_hinting.py
def myfunction(myparameter: int):
    print(myparameter)

myfunction(1)  # prints 1
myfunction("Hello")  # prints Hello # no error
```

- **Type Hinting for Parameters**: The function `myfunction` expects an integer (`int`) as its parameter. However, Python does not enforce this, so passing a string ("Hello") does not raise an error at runtime.

```python:type_hinting/type_hinting.py
def myfunction2(myparameter: int) -> int:
    return myparameter + 1

print(myfunction2(1))  # prints 2
```

- **Type Hinting for Return Values**: The function `myfunction2` expects an integer parameter and indicates that it will return an integer (`-> int`). This helps with understanding what type of value the function should return.

```python:type_hinting/type_hinting.py
def otherfunction(otherparameter: str):
    print(otherparameter)

otherfunction(myfunction2(20))  # prints 21
```

- **Type Compatibility**: The function `otherfunction` expects a string parameter. When calling `otherfunction(myfunction2(20))`, `myfunction2(20)` returns `21`, which is an integer. This works because `print` can handle integers, but it might not be the intended use.

```python:type_hinting/type_hinting.py
print(myfunction2("Hello"))  # TypeError: can only concatenate str (not "int") to str
```

- **Type Error**: Here, `myfunction2("Hello")` raises a `TypeError` because the function tries to add `1` to a string, which is not allowed. This error occurs at runtime, not because of type hinting, but because of the operation inside the function.

### Key Points about Type Hinting:
1. **Syntax**:
    - For parameters: `def function_name(param: type):`
    - For return values: `def function_name(param) -> return_type:`

2. **Static Type Checking**:
    - Tools like `mypy` can be used to check type hints and catch type-related errors before runtime.

3. **Documentation**:
    - Type hints improve code readability and help other developers understand the expected types.

4. **No Runtime Enforcement**:
    - Python does not enforce type hints at runtime. They are purely for documentation and tooling.

### Example with Type Checking:
To enforce type checking, you can use a tool like `mypy`. First, install it:

```sh
poetry add mypy
```

Then, run it on your script:

```sh
poetry run mypy type_hinting.py
```

This will report any type inconsistencies based on the type hints provided.

Output:

```
type_hinting.py:6: error: Argument 1 to "myfunction" has incompatible type "str"; expected "int"  [arg-type]
type_hinting.py:16: error: Argument 1 to "otherfunction" has incompatible type "int"; expected "str"  [arg-type]
type_hinting.py:19: error: Argument 1 to "myfunction2" has incompatible type "str"; expected "int"  [arg-type]
Found 3 errors in 1 file (checked 1 source file)
```

## Factory Design Pattern

The factory design pattern is a ***creational*** design pattern that provides an interface for creating objects in a superclass or **base class**, but allows subclasses to alter the type of objects that will be created. It is useful when you want to encapsulate the object *creation* logic and provide a way to create objects without specifying the exact class of object that will be created.

### Benefits of the Factory Design Pattern

1. **Encapsulation**: It encapsulates the object creation logic, making it easier to modify and extend.

2. **Flexibility**: It allows for the creation of new types of objects without modifying the existing code.

3. **Code Reusability**: It promotes code reusability by encapsulating the object creation logic in a single place.

4. **Decoupling**: It decouples the client code from the object creation logic, making it easier to change the object creation logic without affecting the client code.

### Example 1: Simple Factory

Here's a simple example to illustrate the factory design pattern:

```python:factory_design_pattern/factory.py
class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

class AnimalFactory:
    def get_animal(self, animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            raise ValueError("Invalid animal type")

factory = AnimalFactory()
dog = factory.get_animal("dog")
cat = factory.get_animal("cat")

print(dog.make_sound())  # Output: Woof!
print(cat.make_sound())  # Output: Meow!
```

**Key Points**:
1. **Factory Class**: The `AnimalFactory` class encapsulates the logic for creating different types of `Animal` objects.
2. **Subclasses**: The `Dog` and `Cat` classes are subclasses of `Animal` and implement the `make_sound` method.
3. **Client Code**: The client code (main part of the code) uses the factory to create `Animal` objects without specifying the exact class of object that will be created.

This pattern helps in creating objects in a flexible and extensible way, making it easier to manage and modify the object creation logic.

### Example 2: Abstract Factory using ABCs and Interfaces

Another example using abstruct base classes (ABCs) from `abc` and interfaces: [factory.py](design_pattern_factory/factory.py)

Abstract base classes provide a blueprint for other classes to inherit from, enforcing that derived classes implement certain methods.

Here are the key advantages:

1. **Enforces Implementation**:
   - By using `abstractmethod`, you define methods that must be implemented by any subclass. This helps ensure that certain functionality is provided by all subclasses, making your code more structured and predictable.

2. **Promotes Interface-Like Behavior**:
   - Abstract base classes can be used similarly to interfaces in other programming languages. They define a set of methods that derived classes should implement, without providing an implementation for these methods themselves.

3. **Encourages Consistent APIs**:
   - When multiple subclasses inherit from an abstract base class, they are forced to have the same interface (methods). This consistency is useful when you need to ensure that different objects can be used interchangeably, such as in polymorphism.

4. **Enables Abstract Classes**:
   - Using `ABCMeta` allows you to create classes that cannot be instantiated directly. This is useful when the class serves only as a blueprint and should never be used on its own without being subclassed.


# Proxy Design Pattern

The proxy design pattern is a ***structural*** design pattern that provides a surrogate or placeholder for another object to control access to it. It is useful when you want to add additional functionality to an object without changing its interface.

**Benefits of the Proxy Design Pattern**

1. **Control Access**: It allows you to control access to an object by adding additional functionality before or after the object's methods are called.

2. **Lazy Initialization**: It can be used to delay the creation of an object until it is actually needed, which can improve performance and memory usage.

**Example**

A simple example to illustrate the use of the proxy design pattern: [proxy.py](design_pattern_proxy/proxy.py)

## Decorator vs Proxy
The **Decorator** and **Proxy** design patterns both belong to the *structural* design pattern family and can involve wrapping an object to provide additional functionality. However, they serve different purposes and have distinct usage scenarios. Here’s a breakdown of the key differences:

### 1. **Purpose**

- **Decorator Pattern**:
  - **Adds behavior dynamically**: The primary purpose of the decorator pattern is to **add additional behavior or functionality** to an object dynamically without modifying the object itself or affecting other objects from the same class.
  - It enhances the behavior of the object at runtime, allowing for flexible and scalable functionality additions by stacking multiple decorators.
  
- **Proxy Pattern**:
  - **Controls access to the object**: The proxy pattern is used to provide a **surrogate or placeholder** for another object to control access to it. It manages and controls interactions with the actual object, often providing additional functionality like lazy loading, logging, access control, or caching.
  - The proxy object represents the real object and manages its lifecycle or access.

### 2. **Usage Scenarios**

- **Decorator Pattern**:
  - When you need to **dynamically extend** the behavior of objects in a flexible manner without using inheritance.
  - Often used when behavior can be layered (i.e., you can apply one or more decorators to an object in a chain-like fashion).
  - For example, adding functionality like logging, monitoring, or validation to specific instances of objects.

- **Proxy Pattern**:
  - When you need to **control access** to an object or add functionality related to the object’s lifecycle.
  - It’s used in cases where direct access to the object needs to be managed, e.g., for security reasons, resource management, or when dealing with expensive resources like database connections or remote services.
  - Example scenarios include caching objects, controlling access to sensitive resources, or delaying object creation (lazy initialization).

### 3. **Relationship with the Object**

- **Decorator Pattern**:
  - **Wraps** the object and **extends** its behavior without changing its interface. The decorator has the same interface as the object it decorates and can replace it transparently.
  - Multiple decorators can be combined to add multiple layers of functionality.

- **Proxy Pattern**:
  - **Mediates access** to the object. It acts as a **stand-in** for the object, controlling the interactions and sometimes pre-processing or post-processing requests before passing them on to the actual object.
  - The proxy provides the same interface as the real object, but typically, its main role is not to add behavior but to **restrict, optimize, or defer** access to the object.

### 4. **Real-Life Analogies**

- **Decorator Pattern**: 
  - Think of adding accessories to a car or layers of clothing. You can add as many accessories or layers as you want, and they each augment the car's or person's appearance and functionality.
  - Example: Adding functionality like a sunroof, GPS system, or heated seats to a basic car without modifying the car itself.

- **Proxy Pattern**:
  - Think of a security guard in front of a door. You need to pass through the guard to get to the room. The guard may check your credentials or provide logging, but the main purpose is to control your access to the room.
  - Example: A bank ATM machine acts as a proxy to your bank account, controlling access to funds.

### 5. **Diagram Structure**

- **Decorator**:
  - Decorator class holds a reference to the same interface as the object it decorates, and it adds behavior before or after delegating the work to the object.
  ```
  +---------------+           +---------------+
  |  Component    |<----------|  Decorator    |
  +---------------+           +---------------+
        /\                            /\
        |                            ( )
        |                           Target
  +---------------+  
  |  Concrete     |  
  |  Component    |  
  +---------------+  
  ```

- **Proxy**:
  - Proxy class also holds a reference to the real object but usually performs some operations (e.g., security checks, caching, logging) before or after delegating requests to the real object.
  ```
  +-------------+  
  |  Client     |  
  +-------------+  
        |         
        v  
  +-------------+  
  |   Proxy     |  
  +-------------+  
        |         
        v  
  +-------------+  
  |  RealObject |  
  +-------------+  
  ```

### Summary of Differences:

| **Aspect**               | **Decorator Pattern**                                        | **Proxy Pattern**                                              |
|--------------------------|--------------------------------------------------------------|----------------------------------------------------------------|
| **Purpose**               | Adds new behavior or responsibilities to objects dynamically | Controls access to the real object or adds auxiliary behavior  |
| **Main Focus**            | Enhances the object’s functionality                          | Manages or restricts access to the object                       |
| **When to Use**           | When you want to add or extend behavior at runtime           | When you need to control access, handle expensive resources, or add a level of indirection |
| **Implementation**        | Wraps the object and adds behavior                           | Acts as a stand-in to the real object                           |
| **Example**               | Adding features like logging, validation, caching            | Proxy for remote objects, logging, access control               |

# Singleton Design Pattern

The **Singleton Design Pattern** is a ***creational*** design pattern that ensures a class has only one instance and provides a global point of access to it. It is useful when you need to ensure that a class has a single, shared instance that is accessible globally.

**Benefits of the Singleton Design Pattern**

1. **Ensures a Single Instance**: It guarantees that a class has only one instance and provides a global point of access to it.

2. **Global Access**: It provides a global point of access to the instance, which can be useful when you need to ensure that all parts of the system access the same instance.

3. **Lazy Initialization**: It can be used to delay the creation of an object until it is actually needed, which can improve performance and memory usage.

4. **Encapsulation**: It encapsulates the object creation logic, making it easier to modify and extend.

**Example**

A simple example to illustrate the use of the singleton design pattern: [singleton.py](design_pattern_singleton/singleton.py)

# Composite Design Pattern

The **Composite Design Pattern** is a ***structural*** design pattern that allows you to compose objects into tree structures to represent part-whole hierarchies. It lets clients treat individual objects and compositions of objects uniformly.

**Benefits of the Composite Design Pattern**

1. **Uniformity**: It allows you to treat individual objects and compositions of objects uniformly. This means that you can write code that works with both simple objects and complex objects that contain other objects, without needing to know the difference between them.

2. **Flexibility**: It provides a flexible way to structure and manipulate hierarchical data, such as file systems, organization charts, or menus.

3. **Extensibility**: It allows you to add new types of objects to the hierarchy without modifying the existing code.

**Example**

A simple example to illustrate the use of the composite design pattern: [composite.py](design_pattern_composite/composite.py)
