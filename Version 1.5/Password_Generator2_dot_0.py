import string
import os
#Replacement for the random module, Random is not crytpographically safe, since it uses sudeorandom
import secrets
import numpy as np
#Replacement for the random module, Random is not crytpographically safe, since it uses sudeorandom
from sklearn.utils import shuffle

#Clears up the user-interface
def clear():
    os.system('cls||clear')

#Password function
def run_password_generation2_dot_0():

    #Info
    info = input('   Here you will be able to generate a password\n   I reccomend using atleast 3 of each option\n   On the option where you can add what ever you want to the password, DO NOT use spaces\n\nPress enter to continue')
    password = []

    #This loop stops the code from closing the window if run outside of an code editor.
    while True:
        #This loop makes it so that the code re-runs if and Error occurs.
        while True:
            #Asks the user if they want letters in their password.
            dyw_ABC = input('Do you want your password to contain letters? y/n :')
            print('-----------------------')
            if dyw_ABC == 'y':
                #Uppercase error = re-run loop
                while True:
                    #Asks the user how many uppercase letters the password should contain.
                    amount_ABC_upper = (input('How many uppercase letters should the password contain? :'))
                    if (amount_ABC_upper.isdigit()):
                        #Adds the uppercase letter to the password if it was choosen.
                        for i in range(int(amount_ABC_upper)):
                            #Replacement for random
                            the_letters_upper = ''.join(secrets.choice(string.ascii_uppercase))
                            password.append(the_letters_upper)
                        break
                    #If the amount is not a number, this is run
                    else:
                        print('ERROR! You can only type a number, anything else will result in this error message.')
                        print('-----------------------')
                #Lowercase error = re-run loop
                #Does the same as the code above, but for lowercase letter(s)
                while True:
                    amount_ABC_lower = (input('How many lowercase letters should the password contain? :'))
                    if (amount_ABC_lower.isdigit()):
                        for i in range(int(amount_ABC_lower)):
                            the_letters_lower = ''.join(secrets.choice(string.ascii_lowercase))
                            password.append(the_letters_lower)
                        break
                    else:
                        print('ERROR! You can only type a number, anything else will result in this error message.')
                        print('-----------------------')
                break

            elif dyw_ABC == 'n':
                print('Ok! No letters will be added.')
                print('-----------------------\n')
                break

            #Error message.
            else:
                print('ERROR! You can only type y or n, anything else will result in this error message.')
                print('-----------------------')

        print('-----------------------')


    #Code Divider --------------------------------------------------------------------------------------------------------------------------


        #Makes it so that the code reruns if and Error occurs.
        while True:
            #Asks the user if they want numbers in their password.
            dyw_123 = input('Do you want your password to contain numbers 1-9? y/n :')
            if dyw_123 == 'y':
                #Error loop
                while True:
                    #Asks the user how many letters the password should contain.
                    amount_123 = (input('How many numbers should the password contain? :'))
                    if (amount_123.isdigit()):
                        #Had to use a list becasue .coice and .randbelow did not like (0, 9), despite it being the reccomended way to use it in the secrets library documentation
                        list_123 = ['0','1','2','3','4','5','6','7','8','9']
                        #Adds the numbers to the password.
                        for i in range(int(amount_123)):
                            the_numbers = ''.join(secrets.choice(list_123))
                            password.append(the_numbers)
                        break
                    #Error message.
                    else:
                        print('ERROR! You can only type a number, anything else will result in this error message.')
                        print('-----------------------')
                break
            elif dyw_123 == 'n':
                print('Ok! No letters will be added.')
                break

            #Error message.
            else:
                print('ERROR! You can only type y or n, anything else will result in this error message.')
                print('-----------------------')

        print('-----------------------')


    #Code Divider --------------------------------------------------------------------------------------------------------------------------


        #Makes it so that the code reruns if and Error occurs.
        while True:
            #Asks the user if they want ! @ # $ in their password.
            dyw_symbol = input('Do you want your password to contain the following symbols?   @ ! $ #   y/n :')
            if dyw_symbol == 'y':
                #Error loop
                while True:
                    #Asks the user how many of the aforementioned symbols should be added to the password.
                    amount_symbol = (input('How many symbols should the password contain? :'))
                    if (amount_symbol.isdigit()):
                    #Adds the symbols to the password.
                        for i in range(int(amount_symbol)):
                            #I only want these 4 charaters
                            symbol_list = ['@', '!', '$', '#']
                            rsta = ''.join(secrets.choice(symbol_list))
                            password.append(rsta)
                        break
                    #Error message.
                    else:
                        print('ERROR! You can only type y or n, anything else will result in this error message.')
                        print('-----------------------')
                break                    
            elif dyw_symbol == 'n':
                print('Ok! No symbols will be added.')
                break

            #Error massage.
            else:
                print('ERROR! You can only type y or n, anything else will result in this error message.')
                print('-----------------------')

        print('-----------------------')


    #Code Divider --------------------------------------------------------------------------------------------------------------------------


        #Makes it so that the code reruns if and Error occurs.
        while True:
            #Asks if the user wants to add something specific to the password.
            dyw_special = input('Do you want something specific to be in the password? y/n :')
            
            if dyw_special == 'y':
                #What the user want to be added to the password is typed and added here.
                special_add = input('Type what you want added to the password here :')
                password.append(special_add)
                break
            
            elif dyw_special == 'n':
                print('Ok! Noting special will be added.')
                break
            
            else:
                #Error message.
                print('ERROR! You can only type y or n, anything else will result in this error message.')
                print('-----------------------')

        print('-----------------------')


    #Code Divider --------------------------------------------------------------------------------------------------------------------------


        #Shuffles the password list and prints it.
        shuffled_pass = shuffle(password)
        #Removes all commas spaces and so on from the list print.
        print('This is your password  ',*shuffled_pass, sep = '')
        print('-----------------------')

        #Stops the programm when user is done.
        shutdown = input('Press the enter button too return too main menu :')
        if shutdown == 0:
            clear()
            break
        else:
            clear()
            break


#dyw = Do You Want.
#rsta = Random Symbol To Add.