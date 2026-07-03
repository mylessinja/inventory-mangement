# Inventory Management System (Flask REST API)

## Overview

The Inventory Management System is a Flask-based REST API that allows users to manage products in a retail inventory. The application supports full CRUD (Create, Read, Update, Delete) operations, integrates with the OpenFoodFacts API to retrieve product information by barcode, and provides a Command Line Interface (CLI) for interacting with the system.

This project was developed as part of the **Python REST API with Flask – Inventory Management System Summative Lab**.

---

## Features

* RESTful Flask API
* Full CRUD operations
* CLI application for interacting with the API
* OpenFoodFacts API integration
* Simulated in-memory inventory database
* Error handling for invalid requests and missing products
* Unit testing using pytest (where applicable)

---

## Technologies Used

* Python 3
* Flask
* Requests
* Pytest
* OpenFoodFacts API
* Git & GitHub

---

## Project Structure

```
inventory-system/
│
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── external_api.py
│   └── models.py
│
├── cli/
│   └── cli.py
│
├── tests/
│   └── test_api.py
│
├── data/
│   └── inventory.json
│
├── run.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/inventory-system.git
cd inventory-system
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
```

### 3. Activate the virtual environment

Linux/macOS

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

Start the Flask server:

```bash
python run.py
```

The server runs on:

```
http://127.0.0.1:5000
```

---

## API Endpoints

### Get all inventory items

```
GET /inventory
```

### Get one inventory item

```
GET /inventory/<id>
```

### Create a new inventory item

```
POST /inventory
```

Example JSON:

```json
{
    "name": "Milk",
    "brand": "Dairy Best",
    "price": 2.99,
    "quantity": 15,
    "ingredients_text": "Milk"
}
```

### Update an inventory item

```
PATCH /inventory/<id>
```

Example JSON:

```json
{
    "price": 3.50,
    "quantity": 20
}
```

### Delete an inventory item

```
DELETE /inventory/<id>
```

### Fetch product from OpenFoodFacts

```
GET /external/<barcode>
```

Example:

```
GET /external/737628064502
```

---

## CLI Usage

Start the CLI:

```bash
python cli/cli.py
```

Menu:

```
1. View Inventory
2. View Item by ID
3. Add Item
4. Update Item
5. Delete Item
6. Find Product (OpenFoodFacts)
0. Exit
```

---

## Example CLI Workflow

### Add a Product

```
Choose an option: 3

Name: Coca Cola
Brand: Coca Cola
Price: 2.50
Quantity: 20
```

### View Inventory

```
Choose an option: 1
```

### Update a Product

```
Choose an option: 4
```

### Delete a Product

```
Choose an option: 5
```

### Search OpenFoodFacts

```
Choose an option: 6
```

Enter a product barcode to retrieve product information from the OpenFoodFacts API.

---

## Testing

Run the test suite with:

```bash
pytest
```

The project includes tests for:

* Flask API endpoints
* CLI functionality
* External API integration

---

## Error Handling

The application includes error handling for:

* Invalid inventory IDs
* Missing request data
* Invalid API responses
* Connection failures
* Products not found

---

## Future Improvements

* Persistent database using SQLite or PostgreSQL
* User authentication
* Inventory categories
* Product image support
* Search and filtering
* Web-based frontend

---

## Author

Victor Sinja Wamwoyo

---

## License

This project was created for educational purposes as part of the Python REST API with Flask Summative Lab.
