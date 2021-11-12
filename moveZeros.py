"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.


Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
"""
# time complexity O(n) space complexity O(1)
def moveZeroes(arr):
    # slow_pointer will equal slow
    slow = 0
    for i in range(len(arr)):
        #  If the array[i] does not equal zero
        if arr[i] != 0:
            # Swap the arr[slow] with arr[i] and arr[i] with arr[slow]
            arr[slow], arr[i] = arr[i], arr[slow]
            # increment the slow pointer
            slow += 1
        # return the modified array
    return arr


test_one = moveZeroes([0,1,0,3,12])
test_two = moveZeroes([0])
test_three = moveZeroes([0,0,0,0])
test_four = moveZeroes([1,2,3,4,5])
test_five = moveZeroes([0,0,0,0,1])
test_six = moveZeroes([0,1,2,3,4,5])

print(test_one)
print(test_two)
print(test_three)
print(test_four)
print(test_five)
print(test_six)
