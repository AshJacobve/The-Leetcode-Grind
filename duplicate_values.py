# Sets dont allow for duplicate values. 
# If you try to add a duplicate value to a set, it will simply ignore it. 
# This can be useful for removing duplicates from a list.

def duplicate_values(sums: list):
    if len(set(sums))<len(sums):
        return True
    else:
        return False
    
input1 = [1, 2, 3, 4, 5]
input2 = [1, 2, 3, 4, 5, 1]

if duplicate_values(input1) == True:
    print("Incorrect.")
else:
    print("Correct.")
    
if duplicate_values(input2) == False:
    print("Incorrect.")
else:    
    print("Correct.")
