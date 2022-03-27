class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        _max = 0
        max_so_far = 0
        
        for i in range(len(nums)):
    
            if nums[i] == 1:
                max_so_far += 1
            else:
                _max = max(_max, max_so_far)
                max_so_far = 0
        _max = max(_max, max_so_far)
        return _max
                
            