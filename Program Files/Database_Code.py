from cryptography.fernet import Fernet
import copy
import os

def clear():
    os.system('cls||clear')

#Database Fucntion
def run_database():
    
    print('Note: You have to use the key that encrypted the database, no other key will work.')
    #The database.txt file is encrypted, you have to enter the right key file for it to decrypt, otherwise you'll get gibberish
    #ENCK = ENCryption Key
    ENTER_ENCK = input('Enter the file contain the database encryption key :')
    print('-----------------------')
    #Open and loads the ENC key file
    with open(ENTER_ENCK, 'rb') as mykey:
        key = mykey.read()

    #Fernet is the encryption tool i use, it uses AES encryption (More info in how to use option)
    #ef has no meaning (Or maybe i just can't remember the meaning)
    ef = Fernet(key)

    #Opens and loads The database file
    with open('Database.txt', 'rb') as encrypted_file:
        encrypted = encrypted_file.read()

    #This line take a variable that contains the database data, decrypts it and then decodes it
    decrypted = ef.decrypt(encrypted)
    #Decoder line
    decrypted_decoded = decrypted.decode('utf-8')

    #Loop that stops you from fucking up
    while True:
        clear()

        #WWYLTD = What Would You Like To Do, here you give the program the action you want to perfrom
        WWYLTD = input('What action would you like to preform?\n  1---See the database\n  2---Add to the database\n  3---Remove from the database\n  4---Exit\n\n')
        #If you pick 1, you get
        if WWYLTD == '1':
            clear()

            #Another anti fuck up loop
            while True:

                #prints the database, so the user can view it
                print(decrypted_decoded)
                print('---------------------------')
                #Exit database file
                DB_exit = input('To leave, type exit :')

                if DB_exit == 'exit':
                    break
                else:
                    clear()
                    #Error message
                    print('ERROR! You have to type exit')

        #If you pick 2, you get
        elif WWYLTD == '2':
            clear()

            #Turns the database from a str to a list
            decrypted_decoded_listed = decrypted_decoded.split('\n')

            WTA = input('Type what you want to add here :')

            #turns the datatbase from a list to a string
            decrypted_decoded_listed.append(WTA)
            backslash_n = '\n'
            decrypted_decoded = backslash_n.join(decrypted_decoded_listed)

        #If you pick 3, you get
        elif WWYLTD =='3':
            clear()

            #This line turns the decrypted_decoded variable from a str to a list.
            decrypted_decoded_listed = decrypted_decoded.split('\n')

            #Checks length of list, aka how many values are in the list
            amount_lines = len(decrypted_decoded_listed)
            

            #Adds a number to each value in numerical order
            a = 0
            for i in range(amount_lines):
                a = str(a)
                var = decrypted_decoded_listed[i]
                decrypted_decoded_listed[i] = a + var
                a = int(a)
                a = a+1

            #Prints the list to show you all values with their number
            print(decrypted_decoded_listed)

            #Linjer = lines in swedish, bc I am lazy and couldn't come up with a better var name
            #Here the user types the number of the value that should be removed from the database file
            linjer = int(input('What line should be removed? :'))

            #This Code removes the line the user choose
            del decrypted_decoded_listed[linjer]
            newlista=[]
            a = 0
            b = 1
            for i in decrypted_decoded_listed:
                if a >= 10:
                    b = 2
                else:
                    pass
                newlista.append(i[b:])
                a = a + 1
            decrypted_decoded_listed = newlista

            #This code turns the new edited version of the list (aka the database) from a list to a string, and replaces the old database in the RAM.
            backslash_n = '\n'
            decrypted_decoded = backslash_n.join(decrypted_decoded_listed)
            print('-----------------------')
    
        #If you pick 4, you get
        elif WWYLTD == '4':
            clear()
            pek = Fernet(key)
            decrypted_encoded = decrypted_decoded.encode('utf-8')
            encrypted_encoded = pek.encrypt(decrypted_encoded)
            with open('Database.txt', 'wb') as encrypted_file:
                encrypted_file.write(encrypted_encoded)
            print('You are back at the main menu')
            print('---------------------------\n')
            break

        else:
            clear()
            #Error message
            print('ERROR! You have to type the number corresponding to the action you want to perform')
