class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s={}
        for w in strs:
            key="".join(sorted(w))
            if key not in s:
                s[key]=[]
            s[key].append(w)
        return list(s.values())
