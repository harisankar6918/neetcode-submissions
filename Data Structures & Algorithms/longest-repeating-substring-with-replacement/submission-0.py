class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        m=0
        l=0
        freq={}
        for i in range(len(s)):
            freq[s[i]]=freq.get(s[i],0)+1
            maxfreq=max(freq.values())
            while i-l+1 - maxfreq>k:
                freq[s[l]]-=1
                l+=1
                maxfreq=max(freq.values())
            m=max(m,i-l+1)
        return m

        