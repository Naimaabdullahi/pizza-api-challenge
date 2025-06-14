from server.models import db
from server.app import app
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza

with app.app_context():
    db.drop_all()
    db.create_all()

    r1 = Restaurant(name="Kiki's Pizza", address="123 Flavor St")
    r2 = Restaurant(name="Tony's Pizza", address="456 Cheesy Blvd")

    p1 = Pizza(name="Emma", ingredients="Dough, Tomato Sauce, Cheese")
    p2 = Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni")

    db.session.add_all([r1, r2, p1, p2])
    db.session.commit()

    rp1 = RestaurantPizza(price=5, restaurant_id=r1.id, pizza_id=p1.id)
    rp2 = RestaurantPizza(price=7, restaurant_id=r2.id, pizza_id=p2.id)

    db.session.add_all([rp1, rp2])
    db.session.commit()

    print("Database seeded!")
