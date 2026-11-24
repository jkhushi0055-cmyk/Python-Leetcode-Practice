class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n=len(nums)
        og_num=n
        og_sum=0
        for i in range(1,n+1):
            og_sum+=i
        real_sum=0
        for i in nums:
            real_sum+=i
        missing=(og_sum-real_sum)
        return missing        
        