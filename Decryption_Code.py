from cryptography.fernet import Fernet
 
#Decryption Function
def run_decryption():

    info = input('   Here you will be able to Unencrypt a file.\n   You have too have the key used to encrypt the file to unencrypt it.\n   The encrypted file will remain, and a copy of it will be unencrypted.\n   The copy will be named Unencrypted_Your files name.\n\nPress enter to continue :')

    #user enter the key used to encrypt the file
    ENC_Key = input('Enter the keys file name here :')
    print('-----------------------')
    with open(ENC_Key, 'rb') as mykey:
        key = mykey.read()

    #Fernet is the encryption tool I use, It uses AES encryption
    #ef has no meaning
    ef = Fernet(key)

    #The user enters the encrypted files name
    ENC_File = input('Enter the file name here :')
    print('-----------------------')
    with open(ENC_File, 'rb') as encrypted_file:
        encrypted = encrypted_file.read()

    #Decrypts the file
    decrypted = ef.decrypt(encrypted)

    #Makes a decrypted file version
    with open('Unencrypted_' + ENC_File, 'wb') as decrypted_file:
        decrypted_file.write(decrypted)
    #Confirmation and exit loop
    while True:
        EXIT = input('Your file has been Decrypted, Press enter to go back to main menu :')
        if EXIT == 0:
            print('-----------------------\n')
            break
        else:
            print('-----------------------\n')
            break
    