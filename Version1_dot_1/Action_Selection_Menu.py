from Password_Generator import run_password_generation
from Pincode_Generator import run_pincode_generation
from Database_Code import run_database
from EncryptionKey_Generator import run_ENC_key_generation
from Encryption_Code import run_encryption
from Decryption_Code import run_decryption
from How_To_Use import how_to_use



while True:
    #WDYWTD = What Do You Want To Do
    WDYWTD = input ('Hello! What would you like to do?\n   1---See how to use this program\n   2---Create a Password\n   3---Create a Pincode\n   4---Create an Encryption Key\n   5---See Database\n   6---Encrypt a file\n   7---Decrypt a file\n   8---Stop the program\n\n')
    print('---------------------------')
    if WDYWTD == '1':
        print('You selected 1, See how to use')
        print('---------------------------\n')
        how_to_use()
    elif WDYWTD == '2':
        print('You selected 2, Create a password')
        print('---------------------------\n')
        run_password_generation()
    elif WDYWTD == '3':
        print('You selected 3, Create a pincode')
        print('---------------------------\n')
        run_pincode_generation()
    elif WDYWTD == '4':
        print('You selected 4, Create an encryption key')
        print('---------------------------\n')
        run_ENC_key_generation()
    elif WDYWTD == '5':
        print('You selected 5, See database\n')
        print('---------------------------\n')
        run_database()
    elif WDYWTD == '6':
        print('You selected 6, Encrypt a file')
        print('---------------------------\n')
        run_encryption()
    elif WDYWTD == '7':
        print('You selected 7, Decrypt a file')
        print('---------------------------\n')
        run_decryption()
    elif WDYWTD == '8':
        print('You selected 8, Stop the program')
        print('---------------------------\n')
        break
    else:
        print('ERROR! You have to type the number corresponding to what action you want to preform.')
        print('---------------------------\n')