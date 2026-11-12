class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n=[]
        count=0
        for i in nums:
            if i not in n:
                n.append(i)
                count+=1
        nums[:count]=n        
        return count        
        