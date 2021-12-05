from art import logo
import math
# def greet(name):
#     print(f'Hello {name}')
#     print('How do you do ? ')
#     print('isn\'t the weather nice today ?')


# greet('Angela')


def greet_with(name, location):
    print(f'Hi {name}!')
    print(f'what is like in {location}')


# greet_with('Jesse', 'Missouri')

# * Key word Argument

# greet_with(location='Missouri', name='Jesse')


# * Paint area calculator

# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5


# def paint_calc(height, width, cover):
#     num_of_cans = math.ceil((height * width)/cover)
#     print(f'You\'ll need {num_of_cans} cans of paint.')


# paint_calc(height=test_h, width=test_w, cover=coverage)

# * Prime number

# n = int(input("Check this number: "))


# def prime_checker(number):
#     list = []
#     if n > 1:
#         for i in range(2, n):
#             if(n % i == 0):
#                 list.append(n)
#     else:

#         print(n, "is a prime number")

#     if len(list) > 1:
#         print('is not prime number')
#     else:
#         print("is a prime number")


# prime_checker(number=n)

# ? Caesar Cipher

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)


def caesar(plain_text, shift_amount, cipher_direction):
    end_text = ''

    if cipher_direction == 'decode':
        shift_amount *= -1
    for letter in plain_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position+shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += letter

    print(f'Your {cipher_direction} text is {end_text}')


should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    caesar(plain_text=text, shift_amount=shift, cipher_direction=direction)
    answer = input(
        'Type "yes" if you want to go again> Otherwise type "no" \n')
    if answer != 'yes':
        should_continue = False


# def encrypt(text, shift):
#     encoded_text = ''
#     for letter in text:
#         index_position = alphabet.index(letter)+shift
#         encoded_text += alphabet[index_position]
#     print(f'Your encoded text is {encoded_text}')


# encrypt(text='hello', shift=5)


# def decrypt(text, shift):
#     decoded_text = ''
#     for letter in text:
#         index_position = alphabet.index(letter)-shift
#         decoded_text += alphabet[index_position]
#     print(f'Your decoded text is {decoded_text}')


# decrypt(text='mjqqt', shift=5)
