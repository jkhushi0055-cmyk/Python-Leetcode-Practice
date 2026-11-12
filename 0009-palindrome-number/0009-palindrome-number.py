class Solution:
    def isPalindrome(self, x: int) -> bool:
        copy=x
        rev=0
        while x>0:
            last=x%10
            rev=rev*10+last
            x//=10
        if rev==copy:
            return True
        else:
            return False        

        