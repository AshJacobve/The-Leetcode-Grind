# Finding the missing number in an array of size n containing numbers from 0 to n

def missing_number(nums):
    return sum(range(0,len(nums)+1)) - sum(nums)

nums=[3,0,1]
nums2 = [9,6,4,2,3,5,7,0,1]

print(missing_number(nums))
print(missing_number(nums2))