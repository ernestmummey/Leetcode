# Write a function that reverses a string. The input string is given as an array of characters s.
#   Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) space

#  time complexity O(n) space O(1)
def reverseString(string):
        leftIdx = 0
        rightIdx = len(string) - 1
        while leftIdx < rightIdx:
#       We add the string[rightIdx] to the variable temp 
                temp = string[rightIdx]
#       We then replace the string[startIdx] with the string[leftIdx]
                string[rightIdx] = string[leftIdx]
#       We then use the temp to replace the string[leftIdx]
                string[leftIdx] = temp
#       Then increment each pointer, since the left pointer is going right we increment by one
                leftIdx += 1
#       The right pointer is heading to the left side of the array so we deincrement
                rightIdx -= 1
#   Since we did not use a variable to store the string and instead we modified it in place we will just return the string
        return string

print(reverseString(["h", "e", "l", "l", "o"]))


#  This approach uses the two pointer technique



#  IMPORTANT even though I could have done this with a single for loop, It still requires the use of two pointers; pointerOne = string[char] pointerTwo = string[len(char) - i - 1].
#  This use of the while loop will cut down on the time which would be O(n/2) however due to convention this will still run in O(n)