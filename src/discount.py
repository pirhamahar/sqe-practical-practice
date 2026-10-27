
def calculate_discount(amount):
    if amount < 0:
        raise ValueError("Amount cannot be negative")
    elif amount < 1000:
        return 0
    elif amount <= 5000:
        return amount * 0.10
    else:
        return amount * 0.20
