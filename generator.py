import random


def generate(number, length, chars):
    for pwd in range(number):
        passwords = ''
        for c in range(length):
            passwords += random.choice(chars)
        print(passwords)