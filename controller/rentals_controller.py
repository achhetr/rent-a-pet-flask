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

    if not rental:
        return { "message": "Rental contract does not exist" }

    return rental_schema.dump(rental)

@rental.post("/")
def create_rental():
    try:
        rental_fields = rental_schema.load(request.json)

        # search pet that will be rented
        pet = Pet.query.get(rental_fields["pet_id"])
        # match the primary key
        if pet.user.id == rental_fields["rentee_id"]:
            return { "message": "Mate you cannot rent your own pet" }


        rental = Rental(**rental_fields)
        db.session.add(rental)
        db.session.commit()
    except:
        return { "message": "You are missing information" }

    return rental_schema.dump(rental)

# only allowed things that will be used
# minimise scope
# flask -> django
