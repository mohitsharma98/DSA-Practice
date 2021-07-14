"""Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj = len(nums)//2
        count = {}
        for i in nums:
            if i in count.keys():
                count[i] += 1
            else:
                count[i] = 1
        for i in count.keys():
            if count[i] > maj:
                return i