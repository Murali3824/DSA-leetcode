from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []

        for x in nums1:
            found = False
            next_greater = -1
            for i in range(len(nums2)):
                if nums2[i] == x:
                    for j in range(i + 1, len(nums2)):
                        if nums2[j] > x:
                            next_greater = nums2[j]
                            break
                    break
            result.append(next_greater)

        return result
