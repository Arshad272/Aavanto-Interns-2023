
# open() - it used to open a file in python

# syntax
# variable = open(file_name, mode)
# variable.opeartion()
# variable.close() 

# modes
# r - read
# w - write
# a - append 
file = open('demo.txt', 'r')
# data = file.read()
# print(data)
# line1 = file.readline()
# print(line1)
# line2 = file.readline()
# print(line2)

# readlines() - it will return all the lines of a file in a list, and each line will be consideread as a new element
# lines = file.readlines()
# print(lines[1])

# a = file.read(3)
# print(a) 
# b = file.read(5)
# print(b) 
file.close()


# modes
# r+ - read
# w+ - write
# a+ - append 

file = open('demo.txt', 'r')
file.seek(7)
# Hello\n
line = file.readline()
print(line)
file.close() 