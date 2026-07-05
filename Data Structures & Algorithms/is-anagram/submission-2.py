class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sd = dict()
        td = dict()
        for x in s:
            if x in sd.keys():
                sd[x]+=1
            else:
                sd[x]=1
        for x in t:
            if x in td.keys():
                td[x]+=1
            else:
                td[x]=1
        if len(sd.keys()) != len(td.keys()):
            return False
        for x in sd.keys():
            if x not in td.keys():
                return False
            elif sd[x] != td[x]:
                return False
        return True

        