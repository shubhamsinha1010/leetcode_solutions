class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        final = []
        
        for i in range(numRows):
            temp = []
            for j in range(i+1):
                if j==0 or j==i:
                    temp.append(1)
                else:
                    temp.append(final[i-1][j]+final[i-1][j-1])
            final.append(temp)
        return final