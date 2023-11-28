# w - write mode
# it will create a new file, if the file doesn't exist 
# it will override (replace) the existing data. All your previous data will be deleted 
# here you cannot perform read operation
# file = open("my_demo.txt", "w")
# file.write("Hii")
# file.close()


# a - append 
# it will add the content at the end of the file. If the file is not present then it will create new file and it will add the content to that file. 
# not allowed to perform read operation
# file = open('my_demo.txt', 'a')
# file.write("\nThis written by PYTHON")
# file.close()


# w+ and a+ - you can perform both read and write
# file = open("my_demo.txt", "a+")
# file.write("\nHello")
# data = file.read()
# print(data)
# file.close()