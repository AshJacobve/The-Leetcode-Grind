# Return a list of the number of integers lesser than each number

def count_smaller(nums):
    temp = sorted(nums)
    hashmap = {}

    for i, num in enumerate(temp):
        if num not in hashmap:
            hashmap.put(num, i)