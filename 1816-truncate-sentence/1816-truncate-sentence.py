class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        a = s.split()
        b=a[:k]
        return " ".join(b)
        