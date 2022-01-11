from cryptography.fernet import Fernet

#Encryption function
def run_encryption():

    info = input('   Here you will be able to Encrypt a file\n\nPress enter to continue')
    
    #Asks the user if the have an encryption key
    #DYH = Do You Have
    while True:
        DYH = input('Do you have your own encryptionkey? y/n :')
        print('-----------------------')
        if DYH == 'y':
            #If the user has an encryption key, they will enter it's file name here
            P_keyfile_name = input('Type the keys file name here :')
            print('-----------------------')
            with open(P_keyfile_name, 'rb') as mykey:
                P_keyfile_name = mykey.read()

            #Here the user enters the file name of the file that they want to encrypt
            file_name = input('What file would you like to encrypt? :')
            print('-----------------------')
            with open(file_name, 'rb') as original_file:
                original = original_file.read()

            #Fernet is the encryption tool I use, It uses AES encryption
            pek = Fernet(P_keyfile_name)

            #Encrypts the file
            encrypted = pek.encrypt(original)

            #Anti crash loop
            while True:
                copy_ver = input('Do you want the encrypted file to make an Un-encrypted copy y/n :')
                #The user wants to create a un-encrypted copy
                if copy_ver == 'y':
                    with open('Encrypted_' + file_name, 'wb') as encrypted_file:
                        encrypted_file.write(encrypted)
                        print('Your file has been encrypted')
                        break
                #The user does not want to create a un-encrypted copy
                elif copy_ver == 'n':
                    with open(file_name, 'wb') as encrypted_file:
                        encrypted_file.write(encrypted)
                        print('Your file has been encrypted')
                        print('-----------------------\n')
                        break
                #Error message.
                else:
                    print('ERROR! You have to type y or n')
                    pass
            break

        #If the user doesn't have a key
        elif DYH == 'n':
            print('You have to have a encryption key to encrypt a file\nPlease go and create one using option 4 in the main menu')
            print('---------------------------')
            exit = input('press enter to leave')
            print('---------------------------\n')
            if exit == 0:
                break
            else:
                break

        else:
            #Error message
            print('ERROR! You have to type y or n, anything else will result in this error message.')
    