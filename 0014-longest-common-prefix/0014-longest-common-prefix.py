class Solution:
    def longestCommonPrefix(self, strs): # strs = ["flower","flow","flight"]
        short = min(strs, key=len) # short = "flow"
        res = ""
        for i in range(len(short)):
            for s in strs:
                if s==short:
                    continue
                if s[i]!=short[i]:
                    return res
            res+=short[i]
        return res