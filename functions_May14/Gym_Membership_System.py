members = {}

def register_member(name, plan, payment_status):
    if name in members:
        print(f"Member '{name}' is already registered.")
    else:
        members[name] = {"plan": plan, "payment_status": payment_status}
        print(f"Member '{name}' registered with plan '{plan}' and payment status '{payment_status}'.")

def change_plan(name, new_plan):
    if name in members:
        members[name]["plan"] = new_plan
        print(f"Member '{name}' plan changed to '{new_plan}'.")
    else:
        print(f"Member '{name}' not found.")

def unpaid_members():
    result = []
    for name, info in members.items():
        if info["payment_status"] == "late":
            result.append(name)
    return result
