# This is a sample Python script.
import pickle


# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sample_users = [
        ["user1", "password1"],
        ["user2", "password2"],
        ["user3", "password3"]
    ]

    with open("./users.txt", "w") as users_file:
        for sample_user in sample_users:
            username = sample_user[0]
            password = sample_user[1]
            users_file.write(username + ';' + password + '\n')


    """"with open('./users.txt', 'w') as f:
        pickler = pickle.Pickler(f)
        for sample_user in sample_users:
            pickler.dump(sample_user)"""


def loginFunction():
    userEntry = ""
    foundName = False

    while userEntry == "":
        userEntry = input("Enter your username: \n")
        usersFile = open("users.txt", "r")
        for line in usersFile:
            print("This is the line I read:%s", line, )
            # Read line by line instead of loading the whole file into memory
            # In this case, it won't matter, but it's a good practice to avoid
            # running out of memory if you have reaaaally large files
            line_without_newline = line.rstrip('\n')  # Remove ending \n
            user_record = line_without_newline.split(';')  # Separate into username
            # and password (make the line a list again)
            userName = user_record[0]
            password = user_record[1]
            # Might as well do userName, password = line_without_newline.split(';')
            if userName == userEntry:
                foundName = True
                print("User found. Verifying password.")
                passwordEntry = input("Enter your password: \n")
                if passwordEntry == password:
                    print("Username and passwords are correct")
                    break
                else:
                    print("incorrect")
                    userEntry = ""

        if not foundName:
            print("Username not recognised")
            userEntry = ""


def loginFunction2():
    userEntry = ""

    while userEntry == "":
        userEntry = input("Enter your username: ")
        usersFile = open("users.txt", "r")
        unpickler = pickle.Unpickler(usersFile)
        while True:
            try:
                user_record = unpickler.load()
                userName = user_record[0]
                password = user_record[1]
                if userName == userEntry:
                    print("User found. Verifying password.")
                    passwordEntry = input("Enter your password: ")
                    if passwordEntry == password:
                        print("Username and passwords are correct")
                    else:
                        print("incorrect")
                        userEntry = ""
                    # Watch out for the indentation here!!
                    break  # Break anyway if the username has been found
            except EOFError:
                # Oh oh... the call to `unpickler.load` broke
                # because we reached the end of the file and
                # there's nothing else to load...
                print("Username not recognised")
                userEntry = ""
                break


"""""if __name__ == "__main__":
    loginFunction()"""""

