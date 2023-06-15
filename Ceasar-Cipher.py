alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
#text = input("Type your message:\n").lower()
#shift = int(input("Type the shift number:\n"))
encrypted_text=[]
proceed='yes'

def encrypt(text,shift):
    for i in text:
        position=alphabet.index(i)
        new_position=position+shift
        encrypted_text.append(alphabet[new_position])
    
    for i in encrypted_text:
        print(i,end="")
    print("\n",encrypted_text)

def decrypt(text,shift):
    for i in text:
        position=alphabet.index(i)
        new_position=position-shift
        encrypted_text.append(alphabet[new_position])
    
    for i in encrypted_text:
        print(i,end="")
    print("\n",encrypted_text)

while proceed=="yes":
    if direction=='encode':
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        encrypt(text,shift)
        proceed=input("Want to restart the process? If so enter yes else no ")
    elif direction=='decode':
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        decrypt(text,shift)
        proceed=input("Want to restart the process? If so enter yes else no ")
    else:
        print("Wrong option")
        break
