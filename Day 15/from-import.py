# import module_name

# other ways - 

# alias operation
# as - used for renaming a module
# import module_name as new_name
# import pyautogui as pg 
# pg.alert("Hello")
# pyautogui.alert("Hello") # error 

# from module_name import function_name
# from pyautogui import alert, confirm
# alert("Hello")
# print(confirm("Do you want to continue?"))

# * - it will import all the functions from a module
from pyautogui import * 
from time import sleep
# alert("Hello")
sleep(5)
write("Hello, this is cool!")