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

