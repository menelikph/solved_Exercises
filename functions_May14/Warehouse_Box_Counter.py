warehouse = []

def add_box(box_type, quantity):
    for box in warehouse:
        if box['type'] == box_type:
            return False  # ya existe
    warehouse.append({'type': box_type, 'quantity': quantity})
    return True

def update_quantity(box_type, new_quantity):
    for box in warehouse:
        if box['type'] == box_type:
            box['quantity'] = new_quantity
            return True
    return False

def has_enough(box_type, required_quantity):
    for box in warehouse:
        if box['type'] == box_type:
            return box['quantity'] >= required_quantity
    return False
