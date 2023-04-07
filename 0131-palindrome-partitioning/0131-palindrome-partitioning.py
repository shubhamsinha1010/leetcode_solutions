class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(s):
            return s == s[::-1]
        
        def backtrack(start, partition):
            if start == len(s):
                partitions.append(partition[:])
            else:
                for end in range(start+1, len(s)+1):
                    if is_palindrome(s[start:end]):
                        partition.append(s[start:end])
                        backtrack(end, partition)
                        partition.pop()
        
        partitions = []
        backtrack(0, [])
        return partitions
