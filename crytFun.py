import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)


#ERCRYPT

plain_txt = input("Enter message to encrypt: ")
cipher_txt = ""

for letter in plain_txt:
    i = chars.index(letter)
    cipher_txt += key[i]

print(f"orginal message: {plain_txt}")
print(f"encrypted message: { cipher_txt}")

#DECRYPT

cipher_txt = input("Enter message to decryt: ")
plain_txt = ""

for letter in cipher_txt:
    i = key.index(letter)
    plain_txt += chars[i]

print(f"encrypted message: { cipher_txt}")
print(f"orginal message: {plain_txt}")
















