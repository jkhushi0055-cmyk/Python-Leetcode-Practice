class Solution:
    def greatestLetter(self, s: str) -> str:
        upper_latter="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lower_latter="abcdefghijklmnopqrstuvwxyz"
        ans=""
        for i in range(25,-1,-1):
            upper=upper_latter[i]
            lower=lower_latter[i]
            if upper in s and lower in s:
                ans=upper
                break       
        return ans