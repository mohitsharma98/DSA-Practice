"""Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, return the number of tuples (i, j, k, l) such that:

0 <= i, j, k, l < n
nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0"""

from typing import List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        m = {}
        ans = 0
        n = len(nums1)
        
        for i in range(0, n):
            x = nums1[i]
            for j in range(0, n):
                y = nums2[j]
                
                if (x+y not in m):
                    m[x+y] = 0
                    
                m[x+y] += 1
                
        for i in range(0, n):
            x = nums3[i]
            for j in range(0,n):
                y = nums4[j]
                target = -(x+y)
                if target in m:
                    ans += m[target]
        return ans