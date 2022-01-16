import random


def run_pincode_generation():
    info = input('   Here you will generate a random pincode\n\nPress enter to continue')
    pincode = []

    #This loop stops the code from closing the window if run outside of an code editor.
    while True:
        #Anti crash/Error loop
        while True:
            #hl = How Long
            hl = input('How long should the pin be? :')
            print('-----------------------')
            #Checks if the input is a number(int) or text(str)
            if (hl.isdigit()):
                #Turnes the input into a int, from a str
                hl_int = int(hl)
                #Adds the number(s).
                for i in range(hl_int):
                    the_numbers = random.randint(0, 9)
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
            print('-----------------------\n')
            break
        else:
            print('-----------------------\n')
            break