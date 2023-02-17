from main import ma

class RentalSchema(ma.Schema):
    class Meta:
        fields = ("id", "pet_id", "rentee_id", "time_duration_in_seconds", "amount_in_cents", "rentee", "pet")

        load_only = ["rentee_id", "pet_id"]

    pet = ma.Nested("PetSchema")
    rentee = ma.Nested("UserSchema")


rental_schema = RentalSchema()
rentals_schema = RentalSchema(many=True)
