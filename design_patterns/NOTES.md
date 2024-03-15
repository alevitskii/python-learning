## Design Principles

1. Encapsulate what varies.
2. Favor composition over inheritance.
3. Program to interfaces, not implementations.
4. Strive for loosely coupled designs between objects that interact.
5. Classes should be open for extension but closed for modification.
6. Depend on abstractions. Do not depend on concrete classes.
7. Only talk to your friends.
8. Don’t call us, we’ll call you.
9. A class should have only one reason to change.

## SOLID

1. The **Single-responsibility** principle: "There should never be more than one reason for a class to change." In other words, every class should have only one responsibility.
2. The **Open–closed** principle: "Software entities ... should be open for extension, but closed for modification."
3. The **Liskov substitution** principle: "Functions that use pointers or references to base classes must be able to use objects of derived classes without knowing it."
4. The **Interface segregation** principle: "Clients should not be forced to depend upon interfaces that they do not use."
5. The **Dependency inversion** principle: "Depend upon abstractions, [not] concretes."

## Design Patters

1. **Strategy** - defines a family of algorithms, encapsulates each one, and makes them interchangeable. Strategy lets the algorithm vary independently from clients that use it.
2. **Observer** - defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.
3. **Decorator** - Attach additional responsibilities to an object dynamically. Decorators provide a flexible alternative to subclassing for extending functionality.
4. **Abstract Factory** - Provides an interface for creating families of related or dependent objects without specifying their concrete classes.
5. **Factory Method** - Defines an interface for creating an object, but let subclasses decide which class to instantiate. Factory Method lets a class defer instantiation to the subclasses.
6. **Singleton** - Ensure a class only has one instance and provide a global point of access to it.
7. **Command** - Encapsulates a request as an object, thereby letting you parameterize clients with different requests, queue or log requests, and support undoable operations.
8. **Adapter** - Converts the interface of a class into another interface clients expect. Lets classes work together that couldn’t otherwise because of incompatible interfaces.
9. **Facade** - Provides a unified interface to a set of interfaces in a subsystem. Facade defines a higher-level interface that makes the subsystem easier to use.
10. **Template Method** - Define the skeleton of an algorithm in an operation, deferring some steps to subclasses. Template Method lets subclasses redefine certain steps of an algorithm without changing the algorithm’s structure.
11. **Iterator** - Provide a way to access the elements of an aggregate object sequentially without exposing its underlying implementation.
12. **Composite** - Compose objects into tree structures to represent part-whole hierarchies. Composite lets clients treat individual objects and compositions of objects uniformly.
13. **State** - Allow an object to alter its behavior when its internal state changes. The object will appear to change its class.
14. There are more...
