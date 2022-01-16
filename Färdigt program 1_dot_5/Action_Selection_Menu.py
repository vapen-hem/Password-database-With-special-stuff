from Password_Generator2_dot_0 import run_password_generation2_dot_0
from Pincode_Generator import run_pincode_generation
from Database_Code import run_database
from EncryptionKey_Generator import run_ENC_key_generation
from Encryption_Code import run_encryption
from Decryption_Code import run_decryption
from How_To_Use import how_to_use
import os
import termcolor

#Alows me to color my output, used for the banner
os.system('color')

#Clears up the user-interface
def clear():
    os.system('cls||clear')

#Anti crash/error loop
while True:

    #Banner, to make one, go here (Font, ANSI Shadow) https://manytools.org/hacker-tools/ascii-banner/ 
    banner = """

    ██╗    ██╗██╗███╗   ██╗████████╗██╗  ██╗███████╗██████╗     ███████╗████████╗ ██████╗ ██████╗  █████╗  ██████╗ ███████╗
    ██║    ██║██║████╗  ██║╚══██╔══╝██║  ██║██╔════╝██╔══██╗    ██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗██╔══██╗██╔════╝ ██╔════╝
    ██║ █╗ ██║██║██╔██╗ ██║   ██║   ███████║█████╗  ██████╔╝    ███████╗   ██║   ██║   ██║██████╔╝███████║██║  ███╗█████╗  
    ██║███╗██║██║██║╚██╗██║   ██║   ██╔══██║██╔══╝  ██╔══██╗    ╚════██║   ██║   ██║   ██║██╔══██╗██╔══██║██║   ██║██╔══╝  
    ╚███╔███╔╝██║██║ ╚████║   ██║   ██║  ██║███████╗██║  ██║    ███████║   ██║   ╚██████╔╝██║  ██║██║  ██║╚██████╔╝███████╗
    ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝    ╚══════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝

      Made by vapen_hem#1161 | https://github.com/vapen-hem
      Banner inspired by Ori#6338 | @therealOri_ | https://github.com/therealOri
    """

    print(termcolor.colored(banner, "magenta"))

    #WDYWTD = What Do You Want To Do
    WDYWTD = input('Hello! What would you like to do?\n   1---See how to use this program\n   2---Create a Password\n   3---Create a Pincode\n   4---Create an Encryption Key\n   5---See Database\n   6---Encrypt a file\n   7---Decrypt a file\n   8---Stop the program\n\n')
    print('---------------------------')
    if WDYWTD == '1':
        clear()
        print('You selected 1, See how to use')
        print('---------------------------\n')
        how_to_use()
    elif WDYWTD == '2':
        clear()
        print('You selected 2, Create a password')
        print('---------------------------\n')
        run_password_generation2_dot_0()
    elif WDYWTD == '3':
        clear()
        print('You selected 3, Create a pincode')
        print('---------------------------\n')
        run_pincode_generation()
    elif WDYWTD == '4':
        clear()
        print('You selected 4, Create an encryption key')
        print('---------------------------\n')
        run_ENC_key_generation()
    elif WDYWTD == '5':
        clear()
        print('You selected 5, See database\n')
        print('---------------------------\n')
        run_database()
    elif WDYWTD == '6':
        clear()
        print('You selected 6, Encrypt a file')
        print('---------------------------\n')
        run_encryption()
    elif WDYWTD == '7':
        clear()
        print('You selected 7, Decrypt a file')
        print('---------------------------\n')
        run_decryption()
    elif WDYWTD == '8':
        clear()
        print('You selected 8, Stop the program')
        print('---------------------------\n')
        break
    else:
        clear()
        print('ERROR! You have to type the number corresponding to what action you want to preform.')
        print('---------------------------\n')