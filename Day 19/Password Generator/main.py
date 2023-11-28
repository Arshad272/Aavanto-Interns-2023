
import random  

PASSWORD_STRING = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+-*/`~!@#$%^&*()_+-=[];'.,<>/?"

PASSWORD = ""
usage = input("Enter the website name : ")
try:
    pass_len = int(input("Enter lenght of Password : "))
except ValueError as e:
    print("Invalid Number")
else:
    for i in range(pass_len):
        char = random.choice(PASSWORD_STRING)
        PASSWORD = PASSWORD + char
    data = f"\n\nYour password for {usage} is {PASSWORD}"
    print(data)
    file = open("passwords.txt", "a")
    file.write(data)
    file.close()
finally:
    print("Program Terminated")



    