import random
import string

def generate_password(length=12):
    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits

    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits)
    ]

    remaining_length = length - len(password)
    password += [random.choice(chars) for _ in range(remaining_length)]

    
    random.shuffle(password)

    
    return ''.join(password)

print(generate_password(12))
