from app.models.user import User
from app.models.amenity import Amenity
from app.models.place import Place
from app.models.review import Review
from app.persistence.repository import SQLAlchemyRepository

class HBnBFacade:
    def __init__(self):
        self.user_repo = SQLAlchemyRepository(User)
        self.amenity_repo = SQLAlchemyRepository(Amenity)
        self.place_repo = SQLAlchemyRepository(Place)
        self.review_repo = SQLAlchemyRepository(Review)

    def create_user(self, user_data):
        return self.user_repo.add(User(**user_data))

    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute('email', email)

    def create_amenity(self, amenity_data):
        return self.amenity_repo.add(Amenity(**amenity_data))

    def get_amenity(self, amenity_id):
        return self.amenity_repo.get(amenity_id)

    def get_all_amenities(self):
        return self.amenity_repo.get_all()

    def create_place(self, place_data):
        return self.place_repo.add(Place(**place_data))

    def get_place(self, place_id):
        return self.place_repo.get(place_id)

    def update_place(self, place_id, data):
        return self.place_repo.update(place_id, data)

    def create_review(self, review_data):
        return self.review_repo.add(Review(**review_data))

    def get_reviews_by_place(self, place_id):
        place = self.get_place(place_id)
        return place.reviews if place else []