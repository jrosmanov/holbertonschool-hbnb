# HBnB Project Diagrams

diagramms for HBnb
---

## 1.TASK (High-Level Package Diagram)

mermaid
classDiagram
    direction TB
    class PresentationLayer {
        +UserService
        +PlaceService
        +ReviewService
        +AmenityService
        +API Endpoints
    }
    class BusinessLogicLayer {
        +User
        +Place
        +Review
        +Amenity
        +validate_user()
        +calculate_rating()
    }
    class PersistenceLayer {
        +UserRepository
        +PlaceRepository
        +ReviewRepository
        +AmenityRepository
        +DatabaseOperations()
    }
    PresentationLayer --> BusinessLogicLayer : Facade Pattern
    BusinessLogicLayer --> PersistenceLayer : Database Operations

## 2.TASK (Detailed Class Diagram)
mermaid
classDiagram
    class User {
        +UUID id
        +string name
        +string email
        +string password
        +datetime created_at
        +datetime updated_at
        +register()
        +login()
    }
    class Place {
        +UUID id
        +string name
        +string description
        +float price
        +User owner
        +datetime created_at
        +datetime updated_at
        +add_review(review)
        +calculate_rating()
    }
    class Review {
        +UUID id
        +User user
        +Place place
        +string text
        +int rating
        +datetime created_at
        +datetime updated_at
    }
    class Amenity {
        +UUID id
        +string name
        +string description
        +datetime created_at
        +datetime updated_at
    }
    User "1" -- "0..*" Place : owns
    Place "1" -- "0..*" Review : has
    User "1" -- "0..*" Review : writes
    Place "0..*" -- "0..*" Amenity : provides

## 3.TASK (Diagram Sequence(User Registration))
mermaid
sequenceDiagram
    participant User
    participant API
    participant BusinessLogic
    participant Database
    User->>API: Register(user data)
    API->>BusinessLogic: validate_user_data()
    BusinessLogic->>Database: save_user()
    Database-->>BusinessLogic: confirmation
    BusinessLogic-->>API: return success
    API-->>User: registration success

## 3.TASK (Diagram Sequence(Place Creation))
mermaid
sequenceDiagram
participant User
participant API
participant BusinessLogic
participant Database

User->>API: CreatePlace(place data)
API->>BusinessLogic: validate_place_data()
BusinessLogic->>Database: save_place()
Database-->>BusinessLogic: confirmation
BusinessLogic-->>API: return success
API-->>User: place created

## 3.TASK (Diagram Sequence(Review Submission))
mermaid
sequenceDiagram
participant User
participant API
participant BusinessLogic
participant Database

User->>API: SubmitReview(place_id, review_data)
API->>BusinessLogic: validate_review()
BusinessLogic->>Database: save_review()
Database-->>BusinessLogic: confirmation
BusinessLogic-->>API: return success
API-->>User: review submitted

## 3.TASK (Diagram Sequence(Fetching a List of Places))
mermaid
sequenceDiagram
participant User
participant API
participant BusinessLogic
participant Database

User->>API: GetPlaces(filters)
API->>BusinessLogic: apply_filters()
BusinessLogic->>Database: fetch_places()
Database-->>BusinessLogic: places list
BusinessLogic-->>API: return places
API-->>User: display places