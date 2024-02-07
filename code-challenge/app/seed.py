from models import db, Hero, Power, HeroPower
from app import app

# Create the application context
with app.app_context():
    # Create the database tables
    db.create_all()

    # Create sample heroes
    hero1 = Hero(name="Kamala Khan", super_name="Ms. Marvel")
    hero2 = Hero(name="Doreen Green", super_name="Squirrel Girl")
    hero3 = Hero(name="Gwen Stacy", super_name="Spider-Gwen")

    db.session.add_all([hero1, hero2, hero3])
    db.session.commit()

    # Create sample powers
    power1 = Power(name="Super Strength", description="Gives the wielder super-human strengths")
    power2 = Power(name="Flight", description="Gives the wielder the ability to fly through the skies at supersonic speed")

    db.session.add_all([power1, power2])
    db.session.commit()

    # Associate powers with heroes using HeroPower
    hero_power1 = HeroPower(hero=hero1, power=power1, strength="Strong")
    hero_power2 = HeroPower(hero=hero1, power=power2, strength="Average")
    hero_power3 = HeroPower(hero=hero2, power=power1, strength="Weak")
    hero_power4 = HeroPower(hero=hero3, power=power2, strength="Average")

    db.session.add_all([hero_power1, hero_power2, hero_power3, hero_power4])
    db.session.commit()

    print("Database seeded successfully.")
