import math

def greet(something):
    print(f"Hello Pablo {something}")
    print("Here code Py")
    print("Bye")

def paint_calc(height, width, cover):
    area = height * width
    num_of_cans = math.ceil(area / cover)
    print(num_of_cans)
    
def prime_number(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number")
    else:
        print("It's not a prime number")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def encrypt(main_text, shift_amount):
    # direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    final_text = ""
    for i in main_text:
        position = alphabet.index(i)
        new_position = position + shift_amount
        new_i = alphabet[new_position]
        final_text += new_i
    print(final_text)
    

def decode(final_text, shift_amount):
    final_decode = ""
    for n in final_text:
        position = alphabet.index(n)
        new_position = position - shift_amount
        new_i = alphabet[new_position]
        final_decode += new_i
    print(final_decode)


if __name__ == '__main__':
    # greet("code")
    # test_h = int(input("Height of wall: "))
    # test_w = int(input("Width of wall: "))
    # coverage = 5
    # paint_calc(height=test_h, width=test_w, cover=coverage)
    # n = int(input("Check this number: "))
    # prime_number(number=n)
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    encrypt(main_text = text, shift_amount = shift)
    decode(final_text = text, shift_amount = shift)


    # while direction != -1:
    #     # encrypt
    #     if direction == "encode":
    #     # decode 
    #     elif direction == "decode":
    #         pass
