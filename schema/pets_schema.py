from main import ma
from marshmallow import fields

class PetSchema(ma.Schema):
    class Meta:
        fields = ("id", "type", "user_id", "weight_gms")

    user = fields.Nested("UserSchema")

pet_schema = PetSchema()
pets_schema = PetSchema(many=True)
