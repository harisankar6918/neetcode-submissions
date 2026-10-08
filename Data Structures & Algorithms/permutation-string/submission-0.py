class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n=len(s1)
        windowsize=n
        l=0
        k={}
        q={}
        for i in range(n):
            k[s1[i]]=k.get(s1[i],0)+1
        for j in range(len(s2)):
            q[s2[j]]=q.get(s2[j],0)+1
            if j-l+1 >windowsize:
                q[s2[l]]-=1
                if q[s2[l]]==0:
                    del q[s2[l]]
                l+=1
            if k==q:
                return True
        
        return False
        
                


            
                

