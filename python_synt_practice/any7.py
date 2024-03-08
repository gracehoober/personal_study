def any7(nums):
    """Are any of these numbers a 7? (True/False)"""

    # sort list -> divide and conquor
    nums = nums.sort()


    # binary search implementation -> O(n): worst case is you have to go through whole array
        # half = round down(len(array) / 2)
    # pointers
        # left
        # right
    #   number at half is 7 -> return true
    #   number is less than half
        # right = half, left = start of array

    #   number is greater than half
        # left = half, right = end of array

    # return false

print("should be true", any7([1, 2, 7, 4, 5]))
print("should be false", any7([1, 2, 4, 5]))


"""Bubble Sort
Selection Sort
Insertion Sort"""