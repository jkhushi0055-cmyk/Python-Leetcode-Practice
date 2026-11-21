class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        b=[]
        for i in range(len(number)):
            if number[i]==digit:
                b.append(number[:i]+number[i+1:])
        return(max(b))                