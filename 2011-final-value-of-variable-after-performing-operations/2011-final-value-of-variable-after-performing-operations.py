class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        sums = 0
        for i in operations:
            if i[0]=='+' or i[-1]=='+':
                sums+=1
                
            else:
                sums-=1
                
        return sums
        