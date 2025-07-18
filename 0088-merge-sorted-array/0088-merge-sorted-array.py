class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        #nums1[m:] = nums2
        #nums1.sort()
        i = n-1
        j = m-1
        k = m+n-1
        while i >= 0 and j >= 0:
            if nums1[j] > nums2[i]:
                nums1[k] = nums1[j]
                j -= 1
            else:
                nums1[k] = nums2[i]
                i -= 1
            k -= 1

        while i >= 0:
            nums1[k] = nums2[i]
            k -= 1
            i -= 1
    