class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        m=[]
        for i in nums1:
            for j in nums2:
                if i==j and i not in m:
                    m.append(i)
        return m            

        