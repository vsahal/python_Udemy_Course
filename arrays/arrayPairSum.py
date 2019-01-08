def arrayPairSum(arr, target):

    pairs = 0

    for nums in arr:
        num2 = target - nums
        if num2 in arr:
            pairs += 1

    return int(pairs / 2)
