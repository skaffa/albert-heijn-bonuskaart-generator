import random

def generate_valid_bonuskaart():
    valid_prefixes = [(2621100,2621140), (2622000,2622030), (2622200,2622270), (2623013,2623036)]
    random_range = random.choice(valid_prefixes)
    prefix = str(random.randint(random_range[0], random_range[1]))
    body = ''.join(str(random.randint(0, 9)) for _ in range(5))  # 5 random digits to make 12 total
    partial = prefix + body

    # Calculate the 13th digit (checksum)
    total = 0
    for i, digit in enumerate(partial):
        weight = 3 if i % 2 else 1
        total += int(digit) * weight

    check_digit = (10 - (total % 10)) % 10
    return partial + str(check_digit)


print(generate_valid_bonuskaart())
