class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0

        for element in nums:
            if element != val:
                nums[k] = nums[nums.index(element)]
                k += 1
        return (k)
