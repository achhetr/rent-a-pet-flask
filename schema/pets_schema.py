from main import ma

class PetSchema(ma.Schema):
    class Meta:
        fields = ("id", "type", "user", "user_id", "weight_gms")
        load_only = ["user_id"]

    user = ma.Nested("UserSchema")

pet_schema = PetSchema()
pets_schema = PetSchema(many=True)
