class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows=len(matrix)
        columns=len(matrix[0])
        l=0
        r=rows*columns-1
        while l<=r:
            m=(l+r)//2
            row=m//columns
            column=m%columns
            val=matrix[row][column]
            if val==target:
                return True
            elif val>target:
                r=m-1
            else:
                l=m+1
        return False