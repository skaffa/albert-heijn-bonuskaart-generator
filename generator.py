import random

def generate_valid_bonuskaart():
    prefix = "2623030"  # 7 fixed digits
    body = ''.join(str(random.randint(0, 9)) for _ in range(5))  # 5 random digits to make 12 total
    partial = prefix + body

    # Calculate the 13th digit (checksum)
    total = 0
    for i, digit in enumerate(partial):
        weight = 3 if i % 2 else 1
        total += int(digit) * weight

    check_digit = (10 - (total % 10)) % 10
    return partial + str(check_digit)

# Example usage:
print(generate_valid_bonuskaart())
