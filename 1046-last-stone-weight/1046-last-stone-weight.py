import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        while len(stones)!=1:
            if len(stones)==2 and stones[0]==stones[1]:
                return 0
            a = heapq.nlargest(1,stones)[-1]
            b = heapq.nlargest(2,stones)[-1]
            
            if a==b:
                del stones[stones.index(a)]
                del stones[stones.index(b)]
            
            
            else:
                del stones[stones.index(b)]
                stones[stones.index(a)] = a-b
                
                
        return stones[-1]

                
                
        
        