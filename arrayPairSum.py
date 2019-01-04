def arrayPairSum(arr, target):

    pairs = 0

    for nums in arr:
        num2 = target - nums
        if num2 in arr:
            pairs += 1

    return int(pairs / 2)


print(arrayPairSum([1, 9, 2, 8, 3, 7, 4, 6, 5, 5, 13, 14, 11, 13, -1], 10))
