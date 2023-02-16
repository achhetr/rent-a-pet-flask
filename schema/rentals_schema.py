from main import ma

class RentalSchema(ma.Schema):
    class Meta:
        fields = ("id", "pet_id", "user_id", "time_duration_in_seconds", "amount_in_cents", "rentals")

    rentals = ma.List(ma.Nested("RentalSchema", exclude=("user",)))

user_schema = RentalSchema()
users_schema = RentalSchema(many=True)
