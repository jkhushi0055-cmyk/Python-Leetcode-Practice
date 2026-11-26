class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        freq={}
        for i in nums:
            freq[i]=freq.get(i,0)+1
        for i ,count in freq.items():
            if count==1:
                return i    
        