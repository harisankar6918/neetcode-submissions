class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        c=list(zip(position,speed))
        stack=[]
        c.sort(reverse=True)
        for p,s in c:
            t=(target-p)/s
            if not stack or stack[-1]<t:
                stack.append(t)
        return len(stack)