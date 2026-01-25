## High-Level Architecture

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

```mermaid
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
