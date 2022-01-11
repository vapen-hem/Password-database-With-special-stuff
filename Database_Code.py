from cryptography.fernet import Fernet
import copy

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

    #Fernet is the encryption tool i use, it uses AES encryption
    #ef has no meaning
    ef = Fernet(key)

    #Opens and loads The database file
    with open('Database.txt', 'rb') as encrypted_file:
        encrypted = encrypted_file.read()

    #Decrypts the database file
    decrypted = ef.decrypt(encrypted)

    #Open and loads the database file in write mode
    with open('Database.txt', 'wb') as decrypted_file:
        decrypted_file.write(decrypted)
    
    #Loop that stops you from fucking up
    while True:

        #WWYLTD = What Would You Like To Do, here you give the program the action you want ot perfrom
        WWYLTD = input('What action would you like to preform?\n  1---See the database\n  2---Add to the database\n  3---Remove from the database\n  4---Exit\n\n')
        #If you pick 1, you get
        if WWYLTD == '1':

            #Another anti fuck up loop
            while True:

                #Opens and loads database file in read mode
                with open('Database.txt', 'r') as database:
                    #Shows database file
                    print(database.read())
                #Exit database file
                DB_exit = input('To leave, type exit :')
                print('---------------------------')
                if DB_exit == 'exit':
                    break
                else:
                    #Error message
                    print('ERROR! You have to type exit')

        #If you pick 2, you get
        elif WWYLTD == '2':

            WTA = input('Type what you want to add here :')
            print('-----------------------')
            with open('Database.txt', 'a') as database_write:
                database_write.write(WTA + '\n')

        #If you pick 3, you get
        elif WWYLTD =='3':

            #Opens and loads database file in read mode
            with open('Database.txt', 'r') as fp:
                lines = fp.readlines()
                #Copies the database into a list
                lines_temp = copy.copy(lines)

            #Checks length of list, aka how many values are in the list
            amount_lines = len(lines_temp)

            #Adds a number to each value in numerical order
            a = 0
            for i in range(amount_lines):
                a = str(a)
                var = lines_temp[i]
                lines_temp[i] = a + var
                a = int(a)
                a = a+1

            #Prints the list to show you all values with their number
            print(lines_temp)

            #Linjer = lines in swedish, bc I am lazy and couldn't come up with a better var name
            #Here the user types the number of the value that should be removed from the database file
            linjer = int(input('What line should be removed? :'))
            print('-----------------------')
            #Opens and loads the database file to remove the line choosen above
            with open('Database.txt', 'w') as fp:
                for number, line in enumerate(lines):
                    if number not in [linjer]:
                        fp.write(line)
    
        #If you pick 4, you get
        elif WWYLTD == '4':

            #Re-encrypts the database file with the database key before shuting down the program
            with open('Database.txt', 'rb') as original_file:
                original = original_file.read()
            pek = Fernet(key)
            encrypted = pek.encrypt(original)
            with open('Database.txt', 'wb') as encrypted_file:
                encrypted_file.write(encrypted)
            print('You are going back to the main menu')
            print('---------------------------\n')
            break

        else:
            #Error message
            print('ERROR! You have to type the number corresponding to the action you want to perform')