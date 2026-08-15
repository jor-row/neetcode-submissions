class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        nge2 = []
        i = 0

        while len(nge2) < len(nums2):
            num = nums2[i]
            added = False
            for j in range(i + 1, len(nums2)):
                if nums2[j] > num:
                    nge2.append(nums2[j])
                    added = True
                    break
            if not added:
                nge2.append(-1)

            i += 1

        res = []

        for num in nums1:
            idx = nums2.index(num)
            res.append(nge2[idx])

        return res
            

        