# HBnB Project Diagrams

This file contains all diagrams for HBnb Project!
---

## 1️⃣ High-Level Package Diagram

This diagram shows the **three-layer architecture** of the HBnB application.  
It includes the Presentation Layer (services & API), the Business Logic Layer (models), and the Persistence Layer (database interactions).  
The layers communicate via the **Facade Pattern**

```mermaid
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
```
## 2️⃣ Detailed Class Diagram

This diagram represents the entities in the Business Logic Layer.
It shows User, Place, Review, and Amenity classes with their key attributes, methods, and relationships:

- Users own Places
- Users write Reviews for Places
- Places provide multiple Amenities
```mermaid
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
```
## 3️⃣ Sequence Diagram(User Registration)

This diagram shows the flow of registering a new user:

- User sends registration data to API
- API validates the data via Business Logic Layer
- Business Logic saves the user in the Database
- Confirmation is sent back through API to the User

```mermaid
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
```
## 3️.TASK Sequence Diagram(Place Creation)

This diagram illustrates creating a new place listing:

- User submits place details
- API passes it to Business Logic for validation
- Business Logic saves it to Database
- Confirmation is returned to the User
```mermaid
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
```
## 3️.TASK Sequence Diagram(Review Submission)

This diagram shows how a user submits a review:

- User submits review for a place
- API forwards it to Business Logic for validation
- Business Logic saves the review in the Database
- Confirmation is returned to User
```mermaid
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
```
## 3️⃣ Sequence Diagram(Fetching a List of Places)

This diagram shows how the application fetches a list of places:

- User requests a list with filters
- API forwards the request to Business Logic
- Business Logic fetches data from Database
- List of places is returned to User via API
```mermaid
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
```