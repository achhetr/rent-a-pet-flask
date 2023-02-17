from main import db

class Rental(db.Model):
    __tablename__ = "rentals"

    id = db.Column(db.Integer(), primary_key=True)

    time_duration_in_seconds = db.Column(db.Integer())
    amount_in_cents = db.Column(db.Integer())

    pet_id = db.Column(db.Integer(), db.ForeignKey("pets.id"), nullable=False)

    rentee_id = db.Column(db.Integer(), db.ForeignKey("users.id"), nullable=False)

    rentee = db.relationship('User', backref='rentals')
    pet = db.relationship('Pet', backref='rentals')
