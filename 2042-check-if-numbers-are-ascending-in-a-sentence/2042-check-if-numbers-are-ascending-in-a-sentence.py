class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        s=s.split()
        prev=0
        for i in s:
            if i .isdigit():
                num=int(i)
                if num<=prev:
                    return False
                prev=num
        return True            
        