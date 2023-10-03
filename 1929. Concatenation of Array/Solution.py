class Solution(object):
    def getConcatenation(self, nums):
        ans = []
        times = 2
        while times > 0:
            for i in range(len(nums)):
                ans.append(nums[i])
            times -= 1
        return ans