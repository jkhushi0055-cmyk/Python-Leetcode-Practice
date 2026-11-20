class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        freq={}
        ans=[]
        for i in nums:
            freq[i]=freq.get(i,0)+1
        for i,count in freq.items():
            if count==2:
                ans.append(i) 
        for i in range(1,len(nums)+1):
            if freq.get(i,0)==0:
                ans.append(i)
        return ans                   

        