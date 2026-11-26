class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        m=[]
        for i in nums:
            m.append(i*i)
        m=sorted(m)
        return m    
        