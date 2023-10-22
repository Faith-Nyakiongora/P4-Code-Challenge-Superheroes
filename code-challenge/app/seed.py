from models import db, Hero, Power, HeroPower
from app import app

# Create a Flask app context
with app.app_context():
    # Delete existing data
    db.session.query(HeroPower).delete()
    db.session.query(Hero).delete()
    db.session.query(Power).delete()

    print("🦸‍♀️ Seeding powers...")
    # Create sample powers
    power1 = Power(
        name="Super Strength", description="Gives the wielder super-human strength"
    )
    power2 = Power(
        name="Flight",
        description="Allows the wielder to fly through the skies at supersonic speed",
    )
    power3 = Power(
        name="Superhuman Senses",
        description="Enhances the wielder's senses to a superhuman level",
    )
    power4 = Power(
        name="Elasticity",
        description="Enables the wielder to stretch their body to extreme lengths",
    )

    # Add sample powers to the session
    db.session.add_all([power1, power2, power3, power4])

    print("🦸‍♀️ Seeding heroes...")
    # Create sample heroes
    hero1 = Hero(name="Kamala Khan", super_name="Ms. Marvel")
    hero2 = Hero(name="Doreen Green", super_name="Squirrel Girl")
    hero3 = Hero(name="Gwen Stacy", super_name="Spider-Gwen")
    hero4 = Hero(name="Janet Van Dyne", super_name="The Wasp")
    hero5 = Hero(name="Wanda Maximoff", super_name="Scarlet Witch")
    hero6 = Hero(name="Carol Danvers", super_name="Captain Marvel")
    hero7 = Hero(name="Jean Grey", super_name="Dark Phoenix")
    hero8 = Hero(name="Ororo Munroe", super_name="Storm")
    hero9 = Hero(name="Kitty Pryde", super_name="Shadowcat")
    hero10 = Hero(name="Elektra Natchios", super_name="Elektra")

    # Add sample heroes to the session
    db.session.add_all(
        [hero1, hero2, hero3, hero4, hero5, hero6, hero7, hero8, hero9, hero10]
    )

    print("🦸‍♀️ Adding powers to heroes...")
    # Create sample hero powers
    hero_power1 = HeroPower(hero=hero1, power=power1, strength="Weak")
    hero_power2 = HeroPower(hero=hero1, power=power2, strength="Average")
    hero_power3 = HeroPower(hero=hero2, power=power3, strength="Average")
    hero_power4 = HeroPower(hero=hero3, power=power4, strength="Weak")
    hero_power5 = HeroPower(hero=hero4, power=power2, strength="Strong")

    # Add sample hero powers to the session
    db.session.add_all(
        [hero_power1, hero_power2, hero_power3, hero_power4, hero_power5]
    )

    # Commit the changes to the database
    db.session.commit()

print("🦸‍♀️ Done seeding!")
