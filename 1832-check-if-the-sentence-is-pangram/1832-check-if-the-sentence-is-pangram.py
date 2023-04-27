class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        
        s = {}
        counts=0
        for i in sentence:
            if i not in s:
                s[i]=0
                counts+=1
                
                
        return counts==26
        