
def maxSubArray(arr):

    if len(arr) == 0:
        return 0

    maxSum = arr[0]
    currentSum = arr[0]

    for num in arr[1:]:
        currentSum = max(currentSum + num, num)

        maxSum = max(currentSum, maxSum)

    return maxSum
