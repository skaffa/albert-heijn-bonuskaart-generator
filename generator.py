import random

def is_valid_bonuskaart(code: str) -> bool:
    if not code:
        return False
    if len(code) != 13:
        return False
    if not code.isdigit():
        return False
    if not code.startswith("26"):
        return False
    if code.startswith("0"):
        return False
    total = 0
    weight = 1
    for digit in code:
        total += int(digit) * weight
        weight = 3 if weight == 1 else 1
    return total % 10 == 0

def generate_bonuskaart_code():
    while True:
        base = "26" + "".join(random.choices("0123456789", k=11))
        if is_valid_bonuskaart(base):
            return base

# Example use
print(generate_bonuskaart_code())
