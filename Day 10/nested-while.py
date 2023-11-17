# while loop present inside another while loop

# syntax
# while condition:
#     while condition:
#         code

a = 1
while a <= 3:
    b = 1
    while b <= 3:
        print(a, b)
        b += 1
    a += 1
