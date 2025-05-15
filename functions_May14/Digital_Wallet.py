wallet = []

def add_expense(category, amount):
    wallet.append({"category": category, "amount": amount})
    print(f"Expense of {amount} added to category '{category}'.")

def total_spent():
    total = 0
    for item in wallet:
        total += item["amount"]
    return total

def expense_percentages():
    total = total_spent()
    if total == 0:
        return {}
    percentages = {}
    for item in wallet:
        category = item["category"]
        amount = item["amount"]
        if category not in percentages:
            percentages[category] = 0
        percentages[category] += amount
    for category in percentages:
        percentages[category] = round((percentages[category] / total) * 100, 2) #round es una función que redondea el número a 2 decimales
    return percentages
