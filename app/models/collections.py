from abc import ABC

from app import db

class Collection(db.Model):
    __tablename__ = 'collections'

    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String)
    lower_price_in_cents: int = db.Column(db.Integer)
    medium_price_in_cents: int = db.Column(db.Integer)
    higher_price_in_cents: int = db.Column(db.Integer)

    def __init__(self, name) -> None:
        super().__init__()
        self.name = name
        self.lower_price_in_cents = 0
        self.medium_price_in_cents = 0
        self.higher_price_in_cents = 0

    def get_id(self):
        return str(self.id)

    @property
    def name(self):
        return self.name
    
    @property
    def lower_price_in_cents(self):
        return self.lower_price_in_cents
    
    @property
    def medium_price_in_cents(self):
        return self.medium_price_in_cents
    
    @property
    def higher_price_in_cents(self):
        return self.higher_price_in_cents
    
    @name.setter
    def name(self, new_name):
        # TODO: add name validations
        self.name = new_name

    def update_prices(self):
        # TODO: implement update prices logic
        # probably consuming a API.
        pass
    
class Card(ABC):
    pass