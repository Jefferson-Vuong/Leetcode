class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = nums1
        arr.extend(nums2)
        arr.sort()
        x = (len(arr) - 1) // 2
        if (arr[x] % 2 == 0):
            return arr[x] + arr[x + 1] // 2.0
        else:
            return arr[x]
