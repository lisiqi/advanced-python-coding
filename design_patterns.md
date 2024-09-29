# Design Patterns

Besides the design patterns covered in the repository, there is a more comprehensive list of design patterns [here](https://refactoring.guru/design-patterns). This document is a quick overview of different design patterns.

Design patterns are typically categorized into **three main types**:

1. **Creational Patterns**: These patterns are focused on **how objects are created**. They abstract the instantiation process, making it more flexible by allowing the system to decide which objects to create and when.

2. **Structural Patterns**: These patterns deal with **how objects and classes are composed** to form larger structures, focusing on simplifying relationships between entities and building flexible structures.

3. **Behavioral Patterns**: These patterns are concerned with **how objects interact and communicate** with each other, focusing on improving communication and the delegation of responsibilities among objects.

---

## 1. **Creational Design Patterns**
These patterns provide various ways to instantiate objects while hiding the creation logic, leading to more flexibility when creating objects.

Here are some common **creational patterns**:

- **Factory Method**:
  - Provides an interface for creating objects, but allows subclasses to alter the type of objects that will be created.
  - Example: A `ShapeFactory` creates different shapes like `Circle`, `Square`, etc., based on input without exposing the creation logic.

- **Abstract Factory**:
  - A higher-level factory pattern that creates related families of objects without specifying their concrete classes.
  - Example: A UI kit that creates related UI components like `Buttons`, `TextFields`, and `Dropdowns` for both Windows and Mac platforms.

- **Builder**:
  - Separates the construction of a complex object from its representation, allowing the same construction process to create different representations.
  - Example: Building a complex `House` with different parts like `Roof`, `Walls`, `Doors`, and `Windows` using a builder class.

- **Prototype**:
  - Creates new objects by copying an existing object (prototype) rather than instantiating from scratch.
  - Example: Cloning objects in a game where you have multiple identical units.

- **Singleton**:
  - Ensures a class has only one instance and provides a global point of access to that instance.
  - Example: A `DatabaseConnection` class where only one instance of the connection object exists in the system.

---

## 2. **Structural Design Patterns**
These patterns focus on how classes and objects are composed to form larger structures and relationships while maintaining flexibility and efficiency.

Here are some common **structural patterns**:

- **Adapter**:
  - Converts the interface of a class into another interface that a client expects, allowing incompatible interfaces to work together.
  - Example: Adapting a `LegacySystem` class to be compatible with a new system by wrapping it with an adapter.

- **Bridge**:
  - Decouples an abstraction from its implementation, allowing the two to vary independently.
  - Example: A `Shape` abstraction that can be implemented with different `Rendering` techniques (like 2D or 3D) without the two being tightly coupled.

- **Composite**:
  - Composes objects into tree-like structures to represent part-whole hierarchies, where individual objects and compositions of objects are treated uniformly.
  - Example: A file system where files and directories are both treated as `FileSystemComponent`.

- **Decorator**:
  - Dynamically adds behavior to an object at runtime without altering its structure.
  - Example: Wrapping a `Coffee` object with decorators like `MilkDecorator` or `SugarDecorator` to add new functionality.

- **Facade**:
  - Provides a simplified interface to a complex subsystem, making the subsystem easier to use.
  - Example: A `HomeTheaterFacade` class simplifies interacting with subsystems like the amplifier, DVD player, and projector.

- **Flyweight**:
  - Reduces memory usage by sharing common parts of objects between instances, typically used for handling large numbers of small objects.
  - Example: Reusing objects representing the same character in a text editor.

- **Proxy**:
  - Provides a surrogate or placeholder for another object, controlling access to it.
  - Example: A virtual proxy for an expensive object, such as a large image, to delay its loading until needed.

---

## 3. **Behavioral Design Patterns**
Behavioral patterns focus on improving communication between objects and the delegation of responsibilities. These patterns help define how objects interact and collaborate with one another in a system.

Here are some common **behavioral patterns**:

- **Chain of Responsibility**:
  - Passes a request along a chain of handlers, where each handler either handles the request or passes it to the next handler in the chain.
  - Example: A support system where requests are escalated through different levels (e.g., Level 1, Level 2, and Level 3 support).

- **Command**:
  - Encapsulates a request as an object, thereby allowing for parameterization of clients with different requests, and support for undoable operations.
  - Example: A remote control where each button press is a command object that can be undone or logged.

- **Interpreter**:
  - Defines a grammar for a language and uses an interpreter to interpret sentences in the language.
  - Example: Interpreting mathematical expressions where each operation (like addition, subtraction) is an object.

- **Iterator**:
  - Provides a way to access elements of an aggregate object sequentially without exposing its underlying representation.
  - Example: Iterating through a collection (like a list or array) using an iterator.

- **Mediator**:
  - Reduces direct communication between objects by having them communicate through a mediator, promoting loose coupling.
  - Example: A chatroom where participants send messages to the chatroom, which forwards them to other participants.

- **Memento**:
  - Captures an object’s state and allows it to be restored later, providing undo functionality.
  - Example: Saving the state of a text editor to allow users to undo and redo changes.

- **Observer**:
  - Defines a one-to-many relationship between objects where changes in one object (the subject) notify all dependent objects (observers).
  - Example: A newsletter subscription where multiple subscribers are notified when a new article is published.

- **State**:
  - Allows an object to change its behavior when its internal state changes, appearing as if the object has changed its class.
  - Example: A vending machine that behaves differently when it's out of stock, dispensing an item, or waiting for a customer.

- **Strategy**:
  - Defines a family of algorithms, encapsulates each one, and makes them interchangeable, allowing the algorithm to vary independently from clients.
  - Example: A sorting class that can switch between different sorting strategies like QuickSort, MergeSort, or BubbleSort.

- **Template Method**:
  - Defines the skeleton of an algorithm, with steps that can be redefined by subclasses, allowing specific steps to vary without changing the overall structure.
  - Example: An abstract class that defines steps for preparing a meal, with concrete subclasses implementing specific steps like preparing ingredients or cooking.

- **Visitor**:
  - Represents an operation to be performed on the elements of an object structure, allowing you to define a new operation without changing the classes of the elements.
  - Example: A tax calculation system where different tax calculations can be applied to different types of goods.

---

## Summary of the Three Categories

- **Creational Patterns**: Focus on object creation mechanisms.
- **Structural Patterns**: Focus on object composition and relationships.
- **Behavioral Patterns**: Focus on how objects interact and responsibilities are distributed.

These three categories of patterns—**creational, structural, and behavioral**—cover the broad range of common problems encountered in software design and development.