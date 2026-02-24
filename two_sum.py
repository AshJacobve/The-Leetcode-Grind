# given a list of integers and a target integer, return the indices of the two numbers that add up to the target

def two_sum(nums, target):
    hashmap = {}

    for i in range(len(nums)):
        composite = target - nums[i]
        if composite in hashmap:
            return [hashmap[composite], i]
        else:
            hashmap[nums[i]] = i

list1 = [2,11,7,15]
list2 = [3,3]

print(two_sum(list1,9))
print(two_sum(list2,6))