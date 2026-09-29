class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)
        l=0
        for i in s:
            if i-1 not in s: 
                current=i
                length=1
                while current+1 in s:
                    current+=1
                    length+=1
                l=max(length,l)
        return l