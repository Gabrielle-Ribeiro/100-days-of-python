from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
is_running = True

def caese_cipher(text, shift, direction):
    cipher_text = ""

    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)

            if direction == "encode":
                position = position + shift
                if position > 25:
                    position -= 26

            elif direction == "decode":
                position = position - shift
            
            cipher_text += alphabet[position]
        else:
            cipher_text += letter

    print(f"The {direction}d text is: {cipher_text}")  

print(logo)

while is_running:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26

    caese_cipher(text, shift, direction)

    answer = input("Type 'yes' if you want to go again. Otherwise tipe 'no'.\n").lower()
    if answer == "no":
        is_running = False

print("Goodbye!")