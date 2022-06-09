def encrypt(string):
    cipher = ''
    for char in string:
        if char == ' ':
            cipher += char
        elif char.isupper():
            cipher += chr((ord(char) + 11 - 65) % 26 + 65)
        else:
            cipher += chr((ord(char) + 11 - 97) % 26 + 97)
    return cipher


def decrypt(string):
    cipher = ''
    for char in string:
        if char == ' ':
            cipher += char
        elif char.isupper():
            cipher += chr((ord(char) - 11 - 65) % 26 + 65)
        else:
            cipher += chr((ord(char) - 11 - 97) % 26 + 97)
    return cipher


user_input = input("Please enter a string\n>> ")
print("\nEncrypt or Decrypt?")
Ways = input("e for Encrypt\nd for Decrypt\n>> ")

if Ways == "e":
    print("The new String is ", encrypt(user_input))
elif Ways == "d":
    print("The new String is ", decrypt(user_input))
else:
    print("ERROR")
