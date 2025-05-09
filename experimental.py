# def calculate_gtin13_checksum(number12: str) -> int:
#     total = sum((int(d) * (3 if i % 2 else 1)) for i, d in enumerate(number12))
#     return (10 - total % 10) % 10

# def generate_gtin13_codes(prefix: str, count: int):
#     if len(prefix) != 6:
#         raise ValueError("Prefix must be 6 digits long")
    
#     codes = []
#     for i in range(count):
#         suffix = f"{i:06d}"
#         body = prefix + suffix
#         checksum = calculate_gtin13_checksum(body)
#         full_code = body + str(checksum)
#         codes.append(full_code)
#     return codes

# # Example
# for code in generate_gtin13_codes("262303", 1000):
#     print(code)





import random

def calculate_gtin13_checksum(number12: str) -> int:
    total = sum((int(d) * (3 if i % 2 else 1)) for i, d in enumerate(number12))
    return (10 - total % 10) % 10

def generate_bonuskaart_code():
    # Start with "26", followed by 10 random digits
    base = "26" + "".join(random.choices("0123456789", k=10))
    checksum = calculate_gtin13_checksum(base)
    return base + str(checksum)

# Generate and print one valid Bonuskaart-style GTIN-13 code
print(generate_bonuskaart_code())
