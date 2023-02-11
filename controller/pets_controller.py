from flask import Blueprint, request
from model.pet import Pet
from model.user import User
from schema.pets_schema import pets_schema, pet_schema
from main import db

pet = Blueprint('pets', __name__, url_prefix="/pets")

@pet.get("/")
def get_pets():
    pets = Pet.query.all()
    return pets_schema.dump(pets)

@pet.get("/<int:id>")
def get_pet(id):
    pet = Pet.query.get(id)

    if not pet:
        return { "message": "Don't try to steal my pet" }

    return pet_schema.dump(pet)

@pet.post("/")
def create_pet():
    # try:
    pet_fields = pet_schema.load(request.json)
    pet = Pet(**pet_fields)

    db.session.add(pet)
    db.session.commit()
    # except:
    #     return { "message": "You don't love pets :(" }

    return pet_schema.dump(pet)
