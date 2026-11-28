class Solution:
    def checkString(self, s: str) -> bool:
        a="ba"
        for i in s:
            if a in s:
                return False
        return True        
          


        