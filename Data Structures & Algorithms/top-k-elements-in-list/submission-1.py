class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s={}
        for i in nums:
            s[i]=s.get(i,0)+1
        sorted_items=sorted(s.items(),key=lambda i:i[1],reverse=True)
        ans=[]
        for a,b in sorted_items[:k]:
            ans.append(a)
        return ans
