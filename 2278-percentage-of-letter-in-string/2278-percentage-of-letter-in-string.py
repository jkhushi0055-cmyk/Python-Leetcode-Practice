class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        a=len(s)
        count=0
        for i in s:
            if i in letter:
                count+=1
        percentage=(count/a)*100
        return (int(percentage))    
        