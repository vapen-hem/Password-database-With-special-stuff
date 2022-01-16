def how_to_use():
    #The info
    print('Welcome to How To Use\n\n')
    print("   The program comes with a 'Databse.txt' file, this is where your database will be stored.\n\n   Start by creating a encryption key, by using option 4, The file will have .key at the end.\n   Once that is done, you encrypt the 'Database.txt' file using option 6\n   After that, the program is ready to use.\n\n")
    print("   The database file has to contain the following:\n   This is the database\n   -----------------------\n   'blankspace'\n   'blankspace'\n\n\n   This should be in the database file already, but i reccomend that you make sure it is.\n\n")
    
    #This loop lets you leave this file when you want to
    while True:
        exit = input('Press enter to exit to main menu')
        print('---------------------------\n')
        if exit == 0:
            break
        else:
            break