class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        b=[]
        for i in target:
            b.append(s.count(i)//target.count(i))
        return (min(b))    

        