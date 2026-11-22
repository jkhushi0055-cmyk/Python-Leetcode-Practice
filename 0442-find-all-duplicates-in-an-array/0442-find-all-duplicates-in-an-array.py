class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        freq={}
        b=[]
        for i in nums:
            freq[i]=freq.get(i,0)+1
        for i,count in freq.items():
            if count>=2:
                b.append(i)
        return b        

        