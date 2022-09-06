class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        _sum = 0
        for num in nums:
            _sum += num
            ans.append(_sum)
        return ans