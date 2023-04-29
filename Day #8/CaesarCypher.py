import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# caesar cypher function
def caesar(shift, mess, final=[]):
    for char in mess:
        if char in alphabet:
            pos = alphabet.index(char)
            new_pos = pos + shift
            final += alphabet[new_pos]
        else:
            final += char


print(art.logo)
ask = ""
# Program loop
while ask != "no":
    final = []
    option = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if option == "encode":
        message = input("Type your message: \n")
        shift_num = int(input("\nType your shift number: \n"))
        caesar(shift_num, message, final)
        print(f"Here is your encoded result: {''.join(final)}")
    elif option == "decode":
        message = input("Type the message you want to decrypt: \n")
        shift_num = int(input("\nType the shift number: \n"))
        shift_num *= -1
        caesar(shift_num, message, final)
        print(f"Here is your decoded result: {''.join(final)}")
    else:
        print("\nError!\nTerminating program\nError!\n")
    ask = input("Type 'yes' if you want to go again. Otherwise type'no'. ")
print("Program terminated")
