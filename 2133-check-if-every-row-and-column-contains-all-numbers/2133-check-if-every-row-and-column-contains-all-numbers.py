class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:

        for i in range(len(matrix)):
            s = [i for i in range(1,len(matrix)+1)]
            for j in range(len(matrix[0])):
                if matrix[i][j] in s:
                    s.remove(matrix[i][j])
                    
            if len(s)!=0:
                return False
                    
        for i in range(len(matrix)):
            r = [i for i in range(1,len(matrix)+1)]
            for j in range(len(matrix[0])):
                if matrix[j][i] in r:
                    r.remove(matrix[j][i])
                    
            if len(r)!=0:
                return False
                    
                    
        return True
        