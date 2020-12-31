def findPairSum(array, sum):
    pair_set = set()
    for value in array:
        if value in pair_set:
            return True
        else:
            pair_set.add(sum - value)

    return False

print(findPairSum([1,2,4,4], 8))