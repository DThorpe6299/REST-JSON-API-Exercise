"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DEFAULT_IMAGE = "https://tinyurl.com/demo-cupcake"

class Cupcake(db.Model):
    """Cupcakes."""

    __tablename__ = 'cupcakes'

    id=db.Column(db.Integer, primary_key=True,              autoincrement=True)
    flavor=db.Column(db.Text, nullable=False)
    size=db.Column(db.Text, nullable=False)
    rating=db.Column(db.Float, nullable=False)
    image=db.Column(db.Text, nullable=False, default='https://tinyurl.com/demo-cupcake')

    def serialize(self):
        """Returns a dict representation of todo which we can turn into JSON"""
        return {
            'id': self.id,
            'flavor': self.flavor,
            'size': self.size,
            'rating': self.rating,
            'image': self.image
        }
    
def connect_db(app):
    db.app = app
    db.init_app(app)
