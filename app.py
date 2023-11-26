"""Flask app for Cupcakes"""
from flask import Flask, request, jsonify, render_template
from models import db, connect_db, Cupcake

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "oh-so-secret"

connect_db(app)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/api/cupcakes')
def list_cupcakes():
    """Get data about all cupcakes."""
    all_cupcakes=[cupcake.serialize() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes=all_cupcakes)

@app.route('/api/cupcakes/<int:id>')
def get_cupcake(id):
    """Get data about a single cupcake."""
    cupcake=Cupcake.query.get_or_404(id)
    return jsonify(cupcake=cupcake.serialize())

@app.route('/api/cupcake', methods=['POST'])
def create_cupcake():
    """Create a cupcake with flavor, size, rating and image data from the body of the request."""
    new_cupcake=Cupcake(flavor=request.json["flavor"], size=request.json['size'], rating=request.json['rating'], image=request.json['image'])
    db.session.add(new_cupcake)
    db.session.commit()
    response_json=jsonify(cupcake=new_cupcake.serialize())
    return (response_json, 201)

@app.route('/api/cupcakes/<int:id>', methods=['PATCH'])
def update_cupcake(id):
    """Update a cupcake with the id passed in the URL and flavor, size, rating and image data from the body of the request."""
    cupcake=Cupcake.query.get_or_404(id)
    cupcake.flavor=request.json.get('flavor', cupcake.flavor)
    cupcake.size=request.json.get('size', cupcake.size)
    cupcake.rating=request.json.get('rating', cupcake.rating)
    cupcake.image=request.json.get('image', cupcake.image)
    db.commit()
    return jsonify(cupcake=cupcake.serialize())

@app.route('/api/cupcakes/<int:id>', methods=['DELETE'])
def delete_cupcake(id):
    """Delete cupcake with the id passed in the URL. Respond with JSON like {message: "Deleted"}."""
    cupcake=Cupcake.query.get_or_404(id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message='Deleted')



if __name__ == '__main__':
    app.run(debug=True)
