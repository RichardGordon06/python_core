import random

def generate_login():
    variants_login = ['komarik', 'Pavel', 'oteC', 'zhuchara', 'popolamshik', 'tarelochnica', 'guzno']
    return random.choice(variants_login)

def generate_age():
    return random.randint(12, 100)

def generate_status():
    return random.choice(["ACTIVE", "BLOCKED", "INACTIVE"])

def generate_user():
    login = generate_login()
    age = generate_age()
    status = generate_status()
    user = (login, age, status)
    return {
        "login": generate_login(),
        "age": generate_age(),
        "status": generate_status()
    }