import random
import string

class wordCryt:
#vars
    chars = " " + string.punctuation + string.digits + string.ascii_letters
    chars = list(chars)
    key = chars.copy()

    random.shuffle(key)

#ERCRYPT

def encryt(): 
    input_plain_txt = input("Enter message to encrypt: ")
    cipher_txt = ""

    for letter in input_plain_txt:
        i = wordCryt.chars.index(letter)
        cipher_txt += wordCryt.key[i]

    encryt()

#DECRYPT
def decryt():
    input_cipher_txt = input("Enter message to decryt: ")
    decryt_plain_txt = ""

    for letter in input_cipher_txt:
        i = wordCryt.key.index(letter)
        decryt_plain_txt += wordCryt.chars[i]

    print(f"orginal message: {input_cipher_txt}")
    print(f"encrypted message: {decryt_plain_txt}")
decryt()

















