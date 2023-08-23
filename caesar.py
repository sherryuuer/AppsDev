alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount):
    cipher_text = "" 
    for idx in range(0, len(plain_text)):
        new_idx = alphabet.index(plain_text[idx]) + shift_amount
        if new_idx >= len(alphabet):
            new_idx = new_idx - len(alphabet)
        cipher_text += alphabet[new_idx]
    print(f"The encoded text is {cipher_text}")

#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(cipher_text, shift_amount):
    plain_text = "" 
    for idx in range(0, len(cipher_text)):
        new_idx = alphabet.index(cipher_text[idx]) - shift_amount
        plain_text += alphabet[new_idx]
    print(f"The decoded text is {plain_text}")

  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
  #e.g. 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"


#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
    decrypt(cipher_text=text, shift_amount=shift)
else:
    print("You entered a wrong word.Crushed!")


#make the code better!!!

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(input_direction, input_text, shift_amount):
    output_text = ""
    for letter in input_text:
        position = alphabet.index(letter)
        if input_direction == "encode":
            new_position = position + shift_amount
            if new_position >= len(alphabet):
                new_position = new_position - len(alphabet)
        elif input_direction == "decode":
            new_position = position - shift_amount
        output_text += alphabet[new_position]
    print(f"The {input_direction}d text is {output_text}")

caesar(input_direction=direction, input_text=text, shift_amount=shift)


#make it better and better and debug a little problem great
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(input_direction, input_text, shift_amount):
    output_text = ""
    # this is very interesting be debug this ,because the shift_amount was changed every time we into the loop!!
    if input_direction == "decode":
        shift_amount *= -1
    for letter in input_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        if new_position >= len(alphabet):
            new_position -= len(alphabet)
        # if input_direction == "encode":
        #     new_position = position + shift_amount
        #     if new_position >= len(alphabet):
        #         new_position = new_position - len(alphabet)
        # elif input_direction == "decode":
        #     new_position = position - shift_amount
        output_text += alphabet[new_position]
    print(f"The {input_direction}d text is {output_text}")

caesar(input_direction=direction, input_text=text, shift_amount=shift)



#improve user experience!!
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        #TODO-3: What happens if the user enters a number/symbol/space?
        #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
        #e.g. start_text = "meet me at 3"
        #end_text = "•••• •• •• 3"
        if char not in alphabet:
            end_text += char
        else:
            position = alphabet.index(char)
            new_position = position + shift_amount
            if new_position >= len(alphabet):
                new_position -= len(alphabet)
            end_text += alphabet[new_position]
      
    print(f"Here's the {cipher_direction}d result: {end_text}")

#TODO-1: Import and print the logo from art.py when the program starts.
from art import logo
#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
print(logo)
restart_bool = True
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. 
while restart_bool:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    #TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
    if shift >= len(alphabet):
        shift %= len(alphabet)
    
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if restart == "no":
        restart_bool = False
        print("Goodbye!")