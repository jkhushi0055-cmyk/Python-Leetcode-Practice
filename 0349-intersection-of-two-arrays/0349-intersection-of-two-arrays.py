class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        m=[]
        nums1=set(nums1)
        nums2=set(nums2)
        for i in nums2:
            if i in nums1:
                m.append(i)
        return m        


        