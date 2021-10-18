# Architecture Patterns
This project is meant as a collection of notes on different architecture patterns in Python. 

## Repository Pattern

This is a simple pattern for creating an interface between the database and the business logic.
Keep in mind this about the vocabulary invovled in the repository patterns. Ports are the interface between the application and something else.
Adapters are the implementation that is behind the interface. Generally, if there is an AbstractRepository class, then it is the port. The real repository that is the implementation is the adapter.

## Dependency Inversion

It is the central tenet of most good design patterns to decouple classes as much as possible. Dependency inversion makes the repository pattern possible. 
In this example, SqlAlchemy adapts the AbstractRepository for simple CRUD behavior. 

