# nested - if 
# If block present inside another if block
# used to check one condition depending upon another condition 
# syntax 
# if condition : 
#      code
#      if condition : 
#          code

# if 10 < 5:
#     print("hello 1")
#     if 2 < 1:
#         print("Hello 2") 
#     else:
#         print("Hii")
#     print("hello 3")
# else:
#     print("Hii 2")

if 10 > 5:
    if 4 > 2:
        if 7 < 3:
            print("Hello") 
        print("hello 2")