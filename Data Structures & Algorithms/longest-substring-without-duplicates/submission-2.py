class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {} #last occurance of each char
        l = 0
        out = 0

        for i in range(len(s)):
            if s[i] in mp:
                l = max(mp[s[i]]+1,l)
            mp[s[i]] = i
            out = max(out, i-l+1)
        return out

