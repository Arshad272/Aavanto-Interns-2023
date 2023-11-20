# syntax:
# for var membership range/iterable:
#     code
# else:
#     code

# If the loop is not getting terminated by BREAK keyword then the code present inside else block will get executed

for i in range(1, 11):
    if i == 5:
        break 
    print(i) 
else:
    print("The loop ended normally")