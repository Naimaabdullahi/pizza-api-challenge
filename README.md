# 🍕 Pizza Restaurant API

This is a RESTful API built with **Flask**, **Flask SQLAlchemy**, and **Flask Migrate**. It manages pizzas, restaurants, and their many-to-many relationship through a join table `RestaurantPizza`.

## 📦 Technologies Used

- Python 3
- Flask
- Flask SQLAlchemy
- Flask Migrate
- SQLite (for development)
- Postman (for API testing)

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/Naimaabdullahi/pizza-api-challenge.git
cd pizza-api-challenge
2. Set Up the Virtual Environment
Using pipenv:

bash
Copy
Edit
pipenv install
pipenv shell
Or with venv:

bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
3. Set Up the Database
bash
Copy
Edit
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
4. Seed the Database
bash
Copy
Edit
python server/seed.py
5. Run the Server
bash
Copy
Edit
flask run
Visit http://127.0.0.1:5000

📌 Endpoints
GET /restaurants
Returns a list of all restaurants.

Response:

json
Copy
Edit
[
  {
    "id": 1,
    "name": "Kiki's Pizza",
    "address": "123 Flavor St"
  },
  ...
]
GET /restaurants/<int:id>
Returns a single restaurant with its associated pizzas.

Success Response:

json
Copy
Edit
{
  "id": 1,
  "name": "Kiki's Pizza",
  "address": "123 Flavor St",
  "pizzas": [
    {
      "id": 1,
      "name": "Cheese",
      "ingredients": "Dough, Tomato Sauce, Cheese"
    },
    ...
  ]
}
404 Error Response:

json
Copy
Edit
{ "error": "Restaurant not found" }
DELETE /restaurants/<int:id>
Deletes a restaurant and its associated restaurant_pizzas.

Success:
Status Code 204 No Content

404 Error Response:

json
Copy
Edit
{ "error": "Restaurant not found" }
GET /pizzas
Returns a list of all pizzas.

Response:

json
Copy
Edit
[
  {
    "id": 1,
    "name": "Cheese",
    "ingredients": "Dough, Tomato Sauce, Cheese"
  },
  ...
]
POST /restaurant_pizzas
Creates a new association between a pizza and a restaurant.

Request Body:

json
Copy
Edit
{
  "price": 10,
  "pizza_id": 1,
  "restaurant_id": 2
}
Success Response:

json
Copy
Edit
{
  "id": 1,
  "price": 10,
  "pizza_id": 1,
  "restaurant_id": 2,
  "pizza": {
    "id": 1,
    "name": "Cheese",
    "ingredients": "Dough, Tomato Sauce, Cheese"
  },
  "restaurant": {
    "id": 2,
    "name": "Tony's Pizza",
    "address": "456 Cheesy Blvd"
  }
}
Validation Error Response (Price):

json
Copy
Edit
{ "errors": ["Price must be between 1 and 30"] }
🧪 Postman Collection
You can import the included Postman Collection to test the API manually.

⚠️ Validation Rules
RestaurantPizza.price must be a number between 1 and 30.

🧼 Clean Deletion
When deleting a restaurant, all associated entries in restaurant_pizzas are also removed thanks to:

python
Copy
Edit
relationship("RestaurantPizza", cascade="all, delete-orphan")
📁 Project Structure
bash
Copy
Edit
server/
├── app.py                
├── config.py             
├── seed.py               
├── models/
│   ├── __init__.py       
│   ├── pizza.py
│   ├── restaurant.py
│   └── restaurant_pizza.py
├── controllers/
│   ├── pizza_controller.py
│   ├── restaurant_controller.py
│   └── restaurant_pizza_controller.py
migrations/
📌 Notes
This app is for educational purposes and uses SQLite for simplicity.

In production, use a robust database like PostgreSQL and a WSGI server like Gunicorn.

🧑‍💻 Author
Naima 

vbnet
Copy
Edit
