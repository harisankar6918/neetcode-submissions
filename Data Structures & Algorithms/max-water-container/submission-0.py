class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxarea=0
        maxheight=0
        left=0
        right=len(heights)-1
        while right>left:
            width=right-left
            h=min(heights[left],heights[right])
            area=width*h
            maxarea=max(area,maxarea)
            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1
        return maxarea
