menu = {}

def add_dish(name, price, available):
    if name in menu:
        print(f"Dish '{name}' already exists.")
    else:
        menu[name] = {"price": price, "available": available}
        print(f"Dish '{name}' added.")

def change_availability(name, available):
    if name not in menu:
        print(f"Dish '{name}' not found.")
    else:
        menu[name]["available"] = available
        print(f"Availability of '{name}' changed to {available}.")

def total_available_price():
    total = 0
    for dish in menu.values():
        if dish["available"]:
            total += dish["price"]
    return total
