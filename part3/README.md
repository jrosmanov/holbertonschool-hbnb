erDiagram
    USER ||--o{ PLACE : "owns"}
    USER ||--o{ REVIEW : "writes"}
    PLACE ||--o{ REVIEW : "has"}
    PLACE ||..|{ AMENITY : "includes"}

    USER {
        string id PK
        string email UK
        string password
        boolean is_admin
    }
    PLACE {
        string id PK
        string title
        float price
        string owner_id FK
    }
    REVIEW {
        string id PK
        string text
        int rating
        string user_id FK
        string place_id FK
    }
    AMENITY {
        string id PK
        string name UK
    }