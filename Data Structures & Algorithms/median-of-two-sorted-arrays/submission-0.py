class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Brute force

        combinedList = []

        i, j = 0, 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                combinedList.append(nums1[i])
                i += 1
            else:
                combinedList.append(nums2[j])
                j += 1

        combinedList += nums1[i:]
        combinedList += nums2[j:]
        print(combinedList)
        if not combinedList:
            return -1

        if len(combinedList) % 2 == 1:
            return combinedList[len(combinedList) // 2]

        else :
            return (combinedList[len(combinedList) // 2 - 1] + combinedList[len(combinedList) // 2]) / 2
        return 0