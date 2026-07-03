import requests

BASE_URL = "https://world.openfoodfacts.org/api/v0/product"

def fetch_product(barcode):
    """
    Fetch product details from OpenFoodFacts using a barcode.
    """
    try:
        response = requests.get(f"{BASE_URL}/{barcode}.json", timeout=5)
        response.raise_for_status()

        data = response.json()

        if data.get("status") != 1:
            return None

        product = data.get("product", {})

        return {
            "product_name": product.get("product_name", "Unknown Product"),
            "brands": product.get("brands", "Unknown Brand"),
            "ingredients_text": product.get(
                "ingredients_text",
                "No ingredients listed"
            )
        }

    except requests.RequestException:
        return None
