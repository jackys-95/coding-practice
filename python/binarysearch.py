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

testlist = [3, 5, 6, 8, 11, 12, 14, 15, 17, 18] 
print(binarySearch(testlist, 16))
