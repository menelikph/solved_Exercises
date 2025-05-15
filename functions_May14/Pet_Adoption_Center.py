pets = []

def add_pet(name, species, age):
    for pet in pets:
        if pet["name"] == name:
            print(f"The pet '{name}' already exists.")
            return
    pets.append({"name": name, "species": species, "age": age})
    print(f"Pet '{name}' added successfully.")

def find_by_species(species):
    results = []
    for pet in pets:
        if pet["species"] == species:
            results.append(pet)
    return results

def older_than(min_age):
    older_pets = []
    for pet in pets:
        if pet["age"] > min_age:
            older_pets.append(pet)
    return older_pets
