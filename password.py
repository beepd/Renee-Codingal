import random
import string
def generate_password(length=12):
    if length < 3:
        return "Password length must be at least 3 characters."
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    password_list = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits)
    ]
    all_characters = lower + upper + digits
    for _ in range(length - 3):
        password_list.append(random.choice(all_characters))
    random.shuffle(password_list)
    return "".join(password_list)
password_length = int(input("Enter desired password length: "))
generated_password = generate_password(password_length)
print(f"Generated Password: {generated_password}")