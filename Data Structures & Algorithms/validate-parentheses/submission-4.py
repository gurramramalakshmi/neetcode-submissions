class Solution:
    def isValid(self, s: str) -> bool:
        d = {'(':')','{':'}','[':']'}
        st = []
        for c in s:
            if c in d.keys():
                st.append(c)
            elif st and c == d[st[-1]]:
                st.pop()
            else:
                return False
        return not st

        