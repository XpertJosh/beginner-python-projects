# Login:
# The goal of this project is to allow users to create an account or login to an account.
# Upon creating an account, you will provide a name, password, and response.
# When accessing an account, if the name and password are correct, it will print the response.
# Make sure that if the credentials are incorrect, it doesn't work, and notifies them
# Tips:
# Dictionaries may be useful
isRunning = False

users = {
    # Feel free to instantiate a couple constant keys
    "user": {
        "password": "123",
        "response": "This password is weak."
    }
}

while True:
    processChoice = input('What would you like to do? (login/create/remove/list/exit): ')

    if processChoice == "login":
        username = input("Please enter a username: ")
        if username in users: # If the users dictonary has a key equal to the username variable
            while True: # Creates a loop thats runs until the process is exited
                password = input('Please enter the password: ')
                if users[username]['password'] == password:
                    # If the value of the key password in the username key is equal to the password, continue
                    print(users[username]['response'])
                    break # Exits the loop
                elif 'q' == password:
                    break # If the response is 'q', exit the while function (password loop).
                else: # If the password isn't 'q' or the correct password, prompt them to retry.
                    print('This password is invalid. Please try again.')
        elif username == 'q':
            break; # If the value of the variable 'username' is 'q', exit loop.
        else:
            print('This is an invalid username.')
    elif processChoice == "create":
        while True: # Starts a loop
            username = input("Please enter the username of your account: ")
            if username in users: 
                print('That account has already been created. Please use a different name.')
                break # If account has already been created, exit loop, which exits the process.
            password = input("Please enter the password of your account: ")
            response = input("Please enter the response of your account: ")
            users[str(username)] = {
                "password": password,
                "response": response
            }
            break # At the end of the loop, exit.
    elif processChoice == "remove":
        while True:
            accountName = input("Please type the username of the account you would like to remove: ")
            if accountName in users:
                del users[accountName]
                print("The account '" + accountName + "' has been deleted.")
                break
            elif accountName == 'q':
                break
            else:
                print("This account does not exist. Please enter a valid username.")
                break
    elif processChoice == "list":
        arr = []
        for x in users:
            arr.append(x)
        print(', '.join(arr) + '.')
    elif processChoice == "exit":
        break # Exits the process upon typing exit