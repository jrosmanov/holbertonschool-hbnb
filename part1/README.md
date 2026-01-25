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
