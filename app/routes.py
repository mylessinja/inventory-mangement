from flask import Blueprint, jsonify, request

from flask import Blueprint, jsonify, request
from app.external_api import fetch_product

# Create Blueprint
inventory_bp = Blueprint("inventory", __name__)

# Simulated database (temporary storage)
inventory = [
    {
        "id": 1,
        "name": "Organic Almond Milk",
        "brand": "Silk",
        "price": 3.99,
        "quantity": 10,
        "ingredients_text": "Filtered water, almonds, cane sugar"
    },
    {
        "id": 2,
        "name": "Whole Wheat Bread",
        "brand": "Nature's Own",
        "price": 2.49,
        "quantity": 20,
        "ingredients_text": "Whole wheat flour, water, yeast, salt"
    }
]


# ==========================
# GET ALL ITEMS
# ==========================
@inventory_bp.route("/inventory", methods=["GET"])
def get_inventory():
    return jsonify(inventory), 200


# ==========================
# GET ONE ITEM
# ==========================
@inventory_bp.route("/inventory/<int:item_id>", methods=["GET"])
def get_item(item_id):
    item = next((item for item in inventory if item["id"] == item_id), None)

    if item is None:
        return jsonify({"error": "Item not found"}), 404

    return jsonify(item), 200


# ==========================
# CREATE ITEM
# ==========================
@inventory_bp.route("/inventory", methods=["POST"])
def add_item():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data provided"}), 400

    required_fields = ["name", "brand", "price", "quantity"]

    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"{field} is required"}), 400

    new_item = {
        "id": len(inventory) + 1,
        "name": data["name"],
        "brand": data["brand"],
        "price": data["price"],
        "quantity": data["quantity"],
        "ingredients_text": data.get("ingredients_text", "")
    }

    inventory.append(new_item)

    return jsonify({
        "message": "Item added successfully",
        "item": new_item
    }), 201


# ==========================
# UPDATE ITEM
# ==========================
@inventory_bp.route("/inventory/<int:item_id>", methods=["PATCH"])
def update_item(item_id):

    item = next((item for item in inventory if item["id"] == item_id), None)

    if item is None:
        return jsonify({"error": "Item not found"}), 404

    data = request.get_json()

    if not data:
        return jsonify({"error": "No update data provided"}), 400

    item["name"] = data.get("name", item["name"])
    item["brand"] = data.get("brand", item["brand"])
    item["price"] = data.get("price", item["price"])
    item["quantity"] = data.get("quantity", item["quantity"])
    item["ingredients_text"] = data.get(
        "ingredients_text",
        item["ingredients_text"]
    )

    return jsonify({
        "message": "Item updated successfully",
        "item": item
    }), 200


# ==========================
# DELETE ITEM
# ==========================
@inventory_bp.route("/inventory/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    item = next((item for item in inventory if item["id"] == item_id), None)

    if item is None:
        return jsonify({"error": "Item not found"}), 404

    inventory.remove(item)

    return jsonify({
        "message": "Item deleted successfully"
    }), 200


# ==========================
# EXTERNAL API
# ==========================
@inventory_bp.route("/external/<string:barcode>", methods=["GET"])
def get_external_product(barcode):

    product = fetch_product(barcode)

    if product is None:
        return jsonify({
            "error": "Product not found in OpenFoodFacts"
        }), 404

    return jsonify(product), 200# ✅ MUST be defined EXACTLY like this
inventory_bp = Blueprint("inventory", __name__)

# 🗄️ fake database
inventory = [
    {
        "id": 1,
        "name": "Organic Almond Milk",
        "brand": "Silk",
        "price": 3.99,
        "quantity": 10,
        "ingredients_text": "Filtered water, almonds"
    }
]

# ✅ GET ALL
@inventory_bp.route("/inventory", methods=["GET"])
def get_inventory():
    return jsonify(inventory)

# ✅ GET ONE
@inventory_bp.route("/inventory/<int:item_id>", methods=["GET"])
def get_item(item_id):
    item = next((i for i in inventory if i["id"] == item_id), None)

    if not item:
        return jsonify({"error": "Not found"}), 404

    return jsonify(item)

# ➕ CREATE
@inventory_bp.route("/inventory", methods=["POST"])
def add_item():
    data = request.json

    new_item = {
        "id": len(inventory) + 1,
        "name": data["name"],
        "brand": data.get("brand", ""),
        "price": data["price"],
        "quantity": data["quantity"]
    }

    inventory.append(new_item)

    return jsonify(new_item), 201

# ✏️ UPDATE
@inventory_bp.route("/inventory/<int:item_id>", methods=["PATCH"])
def update_item(item_id):
    item = next((i for i in inventory if i["id"] == item_id), None)

    if not item:
        return jsonify({"error": "Not found"}), 404

    data = request.json

    item["price"] = data.get("price", item["price"])
    item["quantity"] = data.get("quantity", item["quantity"])

    return jsonify(item)

# ❌ DELETE
@inventory_bp.route("/inventory/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    global inventory
    inventory = [i for i in inventory if i["id"] != item_id]

    return jsonify({"message": "Deleted"})
