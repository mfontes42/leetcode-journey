class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: 
            return ""
        pref = strs[0]
        pref_len = len(pref)
        for word in strs[1:]:
            while pref[0:pref_len] != word[0:pref_len]:
                pref_len -= 1
                if pref_len == 0:
                    return ""
        pref = pref[0:pref_len]
        return (pref)