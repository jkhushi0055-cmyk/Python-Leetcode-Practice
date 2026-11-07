class Solution:
    def findGCD(self, nums: list[int]) -> int:
        smallest=min(nums)
        greatest=max(nums)
        for i in range(smallest,0,-1):
            if greatest%i==0 and smallest%i==0:
                return i
                break

        