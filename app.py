"""Flask app for Cupcakes"""

from flask import Flask, request, redirect, jsonify, render_template
from models import db, connect_db, Cupcake
from seed import create_cupcakes

app = Flask(__name__)

app.config['SECRET_KEY'] = "SECRET!"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.drop_all()
db.create_all()
create_cupcakes()

@app.route("/")
def root():
    """Render homepage."""

    cupcakes = Cupcake.query.order_by(Cupcake.flavor).all()
    return render_template("index.html", cupcakes = cupcakes)

@app.route("/api/cupcakes")
def list_cupcakes():
    """Return all cupcakes.

    Returns JSON like:
        {cupcakes: [{id, flavor, size, rating, image}, ...]}
    """

    cupcakes = [cupcake.to_dict() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes=cupcakes)

@app.route("/api/cupcakes/<int:cupcake_id>")
def get_cupcake(cupcake_id):
    """Return specific cupcakes.

    Returns JSON like:
        {cupcakes: [{id, flavor, size, rating, image}]}
    """

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    return jsonify(cupcake=cupcake.to_dict())

@app.route("/api/cupcakes", methods=["POST"])
def create_cupcake():
    """Add new cupcake and return data about new cupcake.

    Returns JSON like:
        {cupcake: [{id, flavor, rating, size, image}]}
    """

    new_cupcake = Cupcake(
        flavor = request.json['flavor'],
        size = request.json['size'],
        rating = request.json['rating'],
        image = request.json['image'] or None)
        
    db.session.add(new_cupcake)
    db.session.commit()

    return (jsonify(cupcake=new_cupcake.to_dict()), 201)