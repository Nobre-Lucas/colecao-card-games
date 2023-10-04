from app import db

import bcrypt

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password_hashed = db.Column(db.String)
    name = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    
    def __init__(self, username, password, name, email) -> None:
        super().__init__()
        self.username = username
        self.password_hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        self.name = name
        self.email = email
        
    def __repr__(self) -> str:
        return f'<User {self.username}>'
    
    @property
    def password(self):
        raise AttributeError('password not readable')
    