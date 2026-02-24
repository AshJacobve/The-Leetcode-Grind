# Check given list for missing numbers from range 1 to n


def find_missing_numbers(nums):
    setnums = set(nums)
    final=[]

    for i in range (1, len(nums)+1):
        if i not in setnums:
            final.append(nums[i])
    return final

test1 = [4,3,2,7,8,2,3,1]

print(find_missing_numbers(test1))



