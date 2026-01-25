# HBnB Technical Documentation

## Introduction
This document provides a high-level and detailed technical overview of the HBnB application.
It describes the system architecture, core business entities, and the interaction flow between
different layers of the application. This documentation serves as a reference for the
implementation phase of the project.

---

## High-Level Architecture

The HBnB application follows a three-layer architecture that separates concerns and improves
maintainability and scalability.

```mermaid
classDiagram
class PresentationLayer {
    <<package>>
    +UserService
    +PlaceService
    +ReviewService
    +AmenityService
    +APIEndpoints()
}

class BusinessLogicLayer {
    <<package>>
    +User
    +Place
    +Review
    +Amenity
}

class PersistenceLayer {
    <<package>>
    +UserRepository
    +PlaceRepository
    +ReviewRepository
    +AmenityRepository
}

PresentationLayer --> BusinessLogicLayer : Facade Pattern
BusinessLogicLayer --> PersistenceLayer : Database Operations

classDiagram
class User {
    +UUID id
    +string email
    +string password
    +datetime created_at
    +datetime updated_at
    +register()
    +updateProfile()
}

class Place {
    +UUID id
    +string name
    +string description
    +datetime created_at
    +datetime updated_at
}

class Review {
    +UUID id
    +string text
    +int rating
    +datetime created_at
}

class Amenity {
    +UUID id
    +string name
}

User "1" --> "0..*" Place : owns
User "1" --> "0..*" Review : writes
Place "1" --> "0..*" Review : receives
Place "*" --> "*" Amenity : has

sequenceDiagram
participant User
participant API
participant Service
participant DB

User->>API: Register account
API->>Service: validate data
Service->>DB: save user
DB-->>Service: success
Service-->>API: response
API-->>User: account created

sequenceDiagram
participant User
participant API
participant Service
participant DB

User->>API: Create place
API->>Service: process request
Service->>DB: save place
DB-->>Service: confirmation
Service-->>API: response
API-->>User: place created

sequenceDiagram
participant User
participant API
participant Service
participant DB

User->>API: Submit review
API->>Service: validate review
Service->>DB: save review
DB-->>Service: success
Service-->>API: response
API-->>User: review added

sequenceDiagram
participant User
participant API
participant Service
participant DB

User->>API: Get places
API->>Service: fetch data
Service->>DB: query places
DB-->>Service: list of places
Service-->>API: response
API-->>User: places list
