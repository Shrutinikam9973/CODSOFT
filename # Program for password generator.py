# Program for password generator
# Program for generating password using ASCII code
import random
import string

def password_generator(size=10, chars=string.ascii_letters + string.digits + string.punctuation):
    return ''.join(random.choice(chars) for _ in range(size))


if __name__ == "__main__":
    print("Generated password is: ", password_generator())