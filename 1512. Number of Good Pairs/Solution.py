class Solution(object):
    def numIdenticalPairs(self, nums):
        r = 0
        for i in range (len(nums)):
            for j in range(len(nums)):
                if nums[i] == nums[j] and i > j:
                    r += 1      
        return r