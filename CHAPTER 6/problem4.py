#to find if username has less than 10 characters

username=input("Enter username: ")

if(len(username)<10):
    print("Characters need to be 10 or more")
else:
    print("Username Accepted")