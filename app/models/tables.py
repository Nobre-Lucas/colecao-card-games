from app import db
from app import login_manager

import bcrypt

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()


class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password_hashed = db.Column(db.String)
    name = db.Column(db.String)
    email = db.Column(db.String, unique=True)

    @property
    def is_authenticated(self):
        return True
    
    @property
    def is_active(self):
        return True
    
    @property
    def is_anonymous(self):
        return False
    
    def get_id(self):
        return str(self.id)
    
    def __init__(self, username, password, name, email) -> None:
        super().__init__()
        self.username = username
        hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        self.password_hashed = hash.decode('utf-8')
        self.name = name
        self.email = email
        
    def __repr__(self) -> str:
        return self.name
    