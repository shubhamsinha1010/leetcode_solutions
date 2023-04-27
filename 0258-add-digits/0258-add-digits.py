class Solution:
    def addDigits(self, num: int) -> int:
        
        a = 0
        while len(str(num))!=1:
            sums=0
            for i in str(num):
                sums+=int(i)
                
            num = sums
                
        return num