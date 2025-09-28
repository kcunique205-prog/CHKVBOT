import random,string
def getstr(data, first, last):
    try:
        start = data.index(first) + len(first)
        end = data.index(last, start)
        return data[start:end]
    except ValueError:
        return None

def generate_username():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=random.randint(6, 10)))

def generate_password():
    return ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=random.randint(12, 16)))

def generate_email():
    username = generate_username()
    domain = random.choice(['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com','aol.com', 'icloud.com'])
    return f'{username}@{domain}'

                   