from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, URLField

class AddCupcakeForm(FlaskForm):
    """Form for adding a cupcake."""

    flavor=StringField("Flavor")
    size=StringField("Size")
    rating=FloatField("Rating")
    image=URLField("Image")
