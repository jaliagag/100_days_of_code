# Create a function that accepts 3 parameters and checks for equality between any two of them.

# Your function should return True if 2 or more of the parameters are equal, 
# and false if none of them are equal to any of the others.


# Extra Credit:

# Modify your function so that strings can be compared to integers if they are equivalent. For example, if the following values are passed to your function:

# 6,5,"5"

# You should modify it so that it returns true instead of false.

# Hint: there's a built in Python function called "int" that will help you convert strings to Integers

"""
THIS FUNCTION ONLY COMPARES SAME TYPES OF DATA
"""

# RETURNS TRUE
# pet = "dog"
# cat = "False"
# dog = "False"

# pet = "dog"
# cat = False
# dog = False

# RETRUSN FALSE
# pet = "dog"
# cat = False
# dog = True

# pet = 5
# cat = "5"
# dog = 5
# name = ""

# def naming (arg1, arg2, arg3):
#     if arg1 == arg3 or arg1 == arg2 or arg2 == arg3:
#         return True
#     elif arg1 != arg3 and arg1 != arg2 and arg2 != arg3:
#         return False
#     else:
#         name = "Simba"
#         return name

"""
^^^^^^^^^^^^^^
THIS FUNCTION ONLY COMPARES SAME TYPES OF DATA
"""

"""
THIS NEXT FUNCTION CONVERTS ALL DATA INTO INTEGERS
"""

# RETURNS TRUE
pet = 6
cat = "5"
dog = 5
name = ""

# # RETURNS FALSE
# pet = 6
# cat = "4"
# dog = 5
# name = ""

def naming (arg1, arg2, arg3):
    arg1 = int(arg1)
    arg2 = int(arg2)
    arg3 = int(arg3)
    if arg1 == arg3 or arg1 == arg2 or arg2 == arg3:
        return True
    elif arg1 != arg3 and arg1 != arg2 and arg2 != arg3:
        return False
    else:
        name = "Simba"
        return name


print(naming(pet, cat, dog))