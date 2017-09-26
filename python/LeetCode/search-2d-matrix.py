class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for row in matrix:
            if len(row) == 0:
                continue
            if target >= row[0] and target <= row[-1]:
                return binarySearch(row, target)
        return False
    
def binarySearch(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist)//2
    if alist[midpoint]==item:
        return True
    else:
        if item<alist[midpoint]:
            return binarySearch(alist[:midpoint],item)
        else:
            return binarySearch(alist[midpoint+1:],item)