class Solution:
    def mostFrequentEven(self, nums: list[int]) -> int:
        b=[]
        for i in nums:
            if i%2==0 :
                b.append(i)
        if len(b)==0:
            return -1     
        max_freq=0
        ans=-1
        for i in set(b):
            freq=b.count(i)
            if freq>max_freq:
                max_freq=freq
                ans=i
            elif freq==max_freq and i<ans:
                ans=i
        return ans           

            