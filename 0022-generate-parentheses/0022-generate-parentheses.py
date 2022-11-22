class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        final = []
        
        def backtrack(left,right):
            
            if left==right==n:
                final.append("".join(stack))
                return
                
            
            if left<n:
                stack.append("(")
                backtrack(left+1,right)
                stack.pop()
                
            if right<left:
                stack.append(")")
                backtrack(left,right+1)
                stack.pop()
                
        
        backtrack(0,0)
        return final