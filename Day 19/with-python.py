# opening a file using with statement

# syntax
# with open('file_name', 'mode') as variable:
    # file operations

# file = open("demo.txt", "w")
# file.write("Hello")
# file.close()

# Outside with block automatically the file will be closed.
with open('demo.txt', 'w') as file:
    file.write("Hello")
    file.write("\nHii")

file.write("\nHii")