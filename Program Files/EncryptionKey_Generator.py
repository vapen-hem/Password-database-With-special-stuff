from cryptography.fernet import Fernet
import os

#Clears up the user-interface
def clear():
    os.system('cls||clear')

#Encryption key generator Function
def run_ENC_key_generation():
    info = input('   Here you will generate an encryption key\n   The tool used to generate the encryption key is called Fernet\n   It uses 128-bit AES encryption in CBC mode, PKCS7 padding and HMAC using SHA256 for authentication\n\nPress enter to continue')
    #Fernet is the encryption tool I use, It uses AES encryption
    #Generates the key
    key = Fernet.generate_key()
    #Here the user enters what the ENC key file should be named
    file_name = input('What should the file containing the key be called? :')
    print('-----------------------')
    with open(file_name + '.key', 'wb') as mykey:
        mykey.write(key)
    #Confirmation and exit loop
    while True:
        EXIT = input('The Encryption key has been generated, Press enter to go back to main menu :')
        if EXIT == 0:
            clear()
            break
        else:
            clear()
            break