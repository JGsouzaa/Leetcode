class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        major = []
        for element in nums:
            if nums.count(element) > len(nums)/3:
                if not element in major:
                    major.append(element)

        return major