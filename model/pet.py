from main import db

class Pet(db.Model):
    __tablename__ = "pets"

    id = db.Column(db.Integer(), primary_key=True)

    weight_gms = db.Column(db.Integer())
    type = db.Column(db.String())

    user_id = db.Column(
        db.Integer(), db.ForeignKey("users.id"), nullable=False
    )
