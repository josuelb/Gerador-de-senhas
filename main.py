import generator
i = True
while i:
    print('Welcome To Your Password Generator')

    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%¨&*().,0123456789'

    number = input('Amount of passoword to generate: ')
    number = int(number)

    if number == 0:
        break

    length = input('You password length: ')
    length = int(length)

    print('\nHere are your passwords:')

    generator.generate(number, length, chars)

    print('\n')