from collections import Counter
from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Count the occurrences of each element in nums1
        count1 = Counter(nums1)
        result = []
        
        # Traverse through nums2 and check for intersection
        for num in nums2:
            # If the number exists in nums1 and its frequency is greater than 0
            if count1[num] > 0:
                result.append(num)
                count1[num] -= 1  # Decrement the count to avoid duplicates
        
        return result
