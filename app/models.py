from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref, validates

db = SQLAlchemy()


class Hero(db.Model):
    __tablename__ = "hero"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    super_name = db.Column(db.String(255), nullable=False)

    powers = db.relationship("Power", secondary="hero_powers", back_populates="heroes")

    def serialize(self):
        serial_powers = [power.serialize() for power in self.powers]
        return {
            "id": self.id,
            "name": self.name,
            "super_name": self.super_name,
            "powers": serial_powers,
        }


class Power(db.Model):
    __tablename__ = "powers"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)

    heroes = db.relationship("Hero", secondary="hero_powers", back_populates="powers")

    def serialize(self):
        return {"id": self.id, "name": self.name, "description": self.description}


class HeroPower(db.Model):
    __tablename__ = "hero_powers"

    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String(20), nullable=False)

    hero_id = db.Column(db.Integer, db.ForeignKey("hero.id"), nullable=False)
    power_id = db.Column(
        db.Integer, db.ForeignKey("powers.id"), nullable=False
    )  # Added ForeignKey for power_id
    hero = db.relationship(
        "Hero", backref=backref("hero_powers", cascade="all, delete-orphan")
    )
    power = db.relationship(
        "Power", backref=backref("hero_powers", cascade="all, delete-orphan")
    )

    def serialize(self):
        return self.hero.serialize()

    @validates("strength")
    def validate_strength(self, key, value):
        if value not in ["Strong", "Weak", "Average"]:
            raise ValueError(
                "Invalid strength value. It must be one of 'Strong', 'Weak', 'Average'"
            )
        return value

    @validates("description")
    def validate_description(self, key, value):
        if len(value) < 20:
            raise ValueError("Description must be at least 20 characters long")
        return value
