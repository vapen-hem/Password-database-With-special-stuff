import secrets
import os


#Removes annoying stuff from the user-interface
def clear():
    os.system('cls||clear')

#pincode function
def run_pincode_generation():
    #info
    info = input('   Here you will generate a random pincode\n\nPress enter to continue')
    #The pincode will be stored here
    pincode = []

    #This loop stops the code from closing the window when done, if run outside of a code editor.
    while True:
        #Anti crash/Error loop
        while True:
            #hl = How Long
            hl = input('How long should the pin be? :')
            print('-----------------------')
            #Checks if the input is a number(int) or text(str)
            if (hl.isdigit()):
                #Had to use a list becasue .coice and .randbelow did not like (0, 9), despite it being the reccomended way to use it in the secrets library documentation
                list_123 = ['0','1','2','3','4','5','6','7','8','9']
                #Adds the numbers to the pincode list
                for i in range(int(hl)):
                    the_numbers = ''.join(secrets.choice(list_123))
                    pincode.append(the_numbers)
                break
            else:
                #Error message
                print('ERROR! You can only type a number, anything else will result in this error message.')
                print('-----------------------')

        #Removes all commas spaces and so on from the list print.
        print('This is your pincode  ',*pincode, sep = '')
        print('-----------------------')

        #Stops the programm when user is done.
        shutdown = input('Press the enter button to go back to main menu :')
        if shutdown == 0:
            clear()
            break
        else:
            clear()
            break