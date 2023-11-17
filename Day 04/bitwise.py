# here operations will be performed on bit level (binary level)
# first we need to convert our decimal number into binary number
# ṭhen we need to perform operation
# then we need to convert result into decimal

# &, |, ~, ^, <<, >>

# & - biwise and
# it will return 1, if both bits are 1
# otherwise it will return 0
# 3 - 0 0 1 1
# 2 - 0 0 1 0
# ------------
# &   0 0 1 0 --> 2
# print(3 & 2)

# | - biwise or
# it will return 0, if both bits are 0
# if any one bit is 1, then it will return 1
# 3 - 0 0 1 1
# 2 - 0 0 1 0
# ------------
# |   0 0 1 1 --> 3
# print(3 | 2)

# ^ - XoR operator
# it will return 1, if both bits are different
# otherwise it will return 0

# 3 - 0 0 1 1
# 2 - 0 0 1 0
# ------------
# ^   0 0 0 1 --> 1
# print(3 ^ 2)

# << - left shift 
# 5 - 0 1 0 1
# 0 1 0 1 0 0 - 20
# print( 5 << 2 )

# >> - right shift 
# bits will be deleted from the right side
# 5 - 0 1 0 1
# 0 1  - 1 
# print( 5 >> 2 )

# ~ - not operator 
# it will give us complement of a given no.
# 7 - 0 1 1 1
print( ~7 )