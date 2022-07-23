from cryptography.fernet import Fernet
import os

# Clears up the user-interface
def clear():
    os.system("cls||clear")


def run_file_encrypt():

    # Info
    info = input(
        "   Here you will be able to Encrypt a file\n\nPress enter to continue"
    )

    # Asks the user if the have an encryption key
    # DYH = Do You Have
    while True:
        DYH = input("Do you have your own encryption key? y/n :")
        print("-----------------------")
        if DYH == "y":
            # If the user has an encryption key, they will enter it's file name here
            P_keyfile_name = input("Type the encryption keys file name here :")
            print("-----------------------")
            with open("encryption/" + P_keyfile_name, "rb") as mykey:
                P_keyfile_name = mykey.read()

            # Here the user enters the file name of the file that they want to encrypt
            file_name = input("What file would you like to encrypt? :")
            print("-----------------------")
            with open("encryption/" + file_name, "rb") as original_file:
                original = original_file.read()

            # Fernet is the encryption tool I use, It uses AES encryption
            pek = Fernet(P_keyfile_name)

            # Encrypts the file
            encrypted = pek.encrypt(original)

            # Anti crash loop
            while True:
                copy_ver = input(
                    "Do you want the encrypted file to make an Un-encrypted copy y/n :"
                )
                print("-----------------------")
                # The user wants to create a un-encrypted copy
                if copy_ver == "y":
                    with open(
                        "encryption/" + "Encrypted_" + file_name, "wb"
                    ) as encrypted_file:
                        encrypted_file.write(encrypted)
                        print("Your file has been encrypted")
                        print("-----------------------")
                        exit1 = input("Press enter to go back to main menu")
                        if exit1 == 0:
                            clear()
                        else:
                            clear()
                        break
                # The user does not want to create a un-encrypted copy
                elif copy_ver == "n":
                    with open("encryption/" + file_name, "wb") as encrypted_file:
                        encrypted_file.write(encrypted)
                        print("Your file has been encrypted")
                        print("-----------------------")
                        exit2 = input("Press enter to go back to main menu")
                        if exit2 == 0:
                            clear()
                        else:
                            clear()
                        break
                # Error message.
                else:
                    print("ERROR! You have to type y or n")
                    pass
            break

        # If the user doesn't have a key
        elif DYH == "n":
            print(
                "You have to have a encryption key to encrypt a file\nPlease go and create one using the generate_key utility under the encryption menu"
            )
            print("---------------------------")
            exit3 = input("press enter to leave")
            print("---------------------------\n")
            clear()
            if exit3 == 0:
                break
            else:
                break

        else:
            # Error message
            print(
                "ERROR! You have to type y or n, anything else will result in this error message."
            )


def run_file_decrypt():

    # Info
    info = input(
        "   Here you will be able to Unencrypt a file.\n   You have too have the key used to encrypt the file to unencrypt it.\n   The encrypted file will remain, and a copy of it will be unencrypted.\n   The copy will be named Unencrypted_Your files name.\n\nPress enter to continue :"
    )

    # user enter the key used to encrypt the file
    ENC_Key = input("Enter the keys file name here :")
    print("-----------------------")
    with open("encryption/" + ENC_Key, "rb") as mykey:
        key = mykey.read()

    # Fernet is the encryption tool I use, It uses AES encryption
    # ef has no meaning
    ef = Fernet(key)

    # The user enters the encrypted files name
    ENC_File = input("Enter the file name here :")
    print("-----------------------")
    with open("encryption/" + ENC_File, "rb") as encrypted_file:
        encrypted = encrypted_file.read()

    # Decrypts the file
    decrypted = ef.decrypt(encrypted)

    # Makes a decrypted file version
    with open("encryption/" + "Unencrypted_" + ENC_File, "wb") as decrypted_file:
        decrypted_file.write(decrypted)
    # Confirmation and exit loop
    while True:
        EXIT = input(
            "Your file has been Decrypted, Press enter to go back to main menu :"
        )
        if EXIT == 0:
            clear()
            break
        else:
            clear()
            break


# Encryption key generator Function
def run_encryption_key_generator():
    info = input(
        "   Here you will generate an encryption key\n   The tool used to generate the encryption key is called Fernet\n   It uses 128-bit AES encryption in CBC mode, PKCS7 padding and HMAC using SHA256 for authentication\n\nPress enter to continue"
    )
    # Fernet is the encryption tool I use, It uses AES encryption
    # Generates the key
    key = Fernet.generate_key()
    # Here the user enters what the ENC key file should be named
    file_name = input("What should the file containing the key be called? :")
    print("-----------------------")
    with open("encryption/" + file_name + ".key", "wb") as mykey:
        mykey.write(key)
    # Confirmation and exit loop
    while True:
        EXIT = input(
            "The Encryption key has been generated, Press enter to go back to main menu :"
        )
        if EXIT == 0:
            clear()
            break
        else:
            clear()
            break
