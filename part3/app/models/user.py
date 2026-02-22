from app import db, bcrypt
from app.models.base import BaseModel
import re

class User(BaseModel):
    __tablename__ = 'users'

    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if 'password' in kwargs:
            self.password = self.hash_password(kwargs['password'])

    def hash_password(self, password):
        return bcrypt.generate_password_hash(password).decode('utf-8')

    def verify_password(self, password):
        return bcrypt.check_password_hash(self.password, password)

    @staticmethod
    def validate_email(email):
        email_regex = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        return re.match(email_regex, email) is not None

places = db.relationship('Place', backref='owner', lazy=True)
reviews = db.relationship('Review', backref='author', lazy=True)