class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        paragraph=re.sub(r'[^\w\s]',' ',paragraph)
        paragraph=paragraph.lower().split()
        freq={}
        for i in paragraph:
            if i not in banned:
                freq[i]=freq.get(i,0)+1
        max=0
        max_word=""        
        for i,count in freq.items():
            if count>max:
                max=count
                max_word=i
        return max_word        



                        

        