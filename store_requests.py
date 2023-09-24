from my_requests import MyRequests


# Store
def place_order(order_id, pet_id, quantity, ship_date, status, complete):
    """
    Place an order for a pet
    Order Status Enum:
    [ placed, approved, delivered ]
    """
    payload = {
        "id": order_id,
        "petId": pet_id,
        "quantity": quantity,
        "shipDate": ship_date,
        "status": status,
        "complete": complete
    }
    url = f"store/order"
    return MyRequests.post(url, json=payload)


def find_purchase_by_id(order_id):
    """
    Find purchase order by ID. For valid response try integer IDs with value >= 1 and <= 10. Other values will generated exceptions
    """
    url = f"store/order/{order_id}"
    return MyRequests.get(url)


def delete_purchase_by_id(order_id):
    """
    Delete purchase order by ID
    """
    url = f"store/order/{order_id}"
    return MyRequests.delete(url)


def return_inventory():
    """
    Returns pet inventories by status
    """
    url = f"store/inventory"
    return MyRequests.get(url)
