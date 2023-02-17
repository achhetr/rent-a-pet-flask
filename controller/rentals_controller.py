from flask import Blueprint, request
from model.rental import Rental
from model.pet import Pet
from schema.rentals_schema import rentals_schema, rental_schema
from main import db

rental = Blueprint('rentals', __name__, url_prefix="/rentals")

@rental.get("/")
def get_rentals():
    rentals = Rental.query.all()
    return rentals_schema.dump(rentals)


@rental.get("/<int:id>")
def get_rental(id):
    rental = Rental.query.get(id)
    return rental_schema.dump(rental)


@rental.post("/")
def create_rental():
    rental_fields = rental_schema.load(request.json)

    pet = Pet.query.get(rental_fields["pet_id"])

    if pet.user.id == rental_fields["rentee_id"]:
        return { "message": "You cannot rent your own pet"}

    print(rental_fields)

    rental = Rental(**rental_fields)

    db.session.add(rental)
    db.session.commit()

    return rental_schema.dump(rental)

