class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row,col = len(board),len(board[0])
        path = set()
        def dfs(r,c,i):
            if i==len(word):
                return True
            
            if r<0 or c<0 or r>=len(board) or c>=len(board[0]) or (r,c) in path or board[r][c]!=word[i]:
                return False
            
            path.add((r,c))
            
            res = (dfs(r,c+1,i+1) or
                  dfs(r+1,c,i+1) or
                  dfs(r-1,c,i+1) or
                  dfs(r,c-1,i+1))
            path.remove((r,c))
            return res
        word_dict = Counter(word)
        board_dict = Counter(itertools.chain.from_iterable(board))
        if any(count>board_dict[char] for char,count in word_dict.items()):
            return False
        #if board_dict[word[0]]>board_dict[word[-1]]:
            #word=
        for r in range(row):
            for c in range(col):
                if dfs(r,c,0): return True