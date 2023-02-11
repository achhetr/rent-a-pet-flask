from main import ma

class UserSchema(ma.Schema):
    class Meta:
        fields = ("id", "username", "verified", "mobile_number", "post_code")

user_schema = UserSchema()
users_schema = UserSchema(many=True)
