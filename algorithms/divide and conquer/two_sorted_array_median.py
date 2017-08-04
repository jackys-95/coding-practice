def two_sorted_arrays_median(a, b):
    '''
    Gets the median from sorted array a of length n
    and sorted array b of length m using modified
    binary search (O(log(n + m)))
    '''
    median_a = get_median(a)
    median_b = get_median(b)
    length_a = len(a)
    length_b = len(b)
    median = None
    
    if (median_a == median_b):
        median = median_a
    else:
        if (len(a) == 1 and len(b) == 1):
            a.append(b[0])
            median = get_median(a)
        elif (len(a) == 2 and len(b) == 2):
            median = median_of_four_elements(a, b)
        elif (median_a > median_b):
            median = two_sorted_arrays_median(a[0:calculate_slice_index(length_a)], \
                                              b[calculate_slice_index(length_b):])
        else:
            median = two_sorted_arrays_median(b[0:calculate_slice_index(length_b)], \
                                              a[calculate_slice_index(length_a):])
    return median

def median_of_four_elements(a, b):
    '''
    Finds the two middle elements and calculates median
    '''
    max_num = (max(a[0], max(a[1], max(b[0], b[1]))))
    min_num = (min(a[0], min(a[1], min(b[0], b[1]))))
    return (a[0] + a[1] + b[0] + b[1] - max_num - min_num) / 2.0
def calculate_slice_index(length):
    if (length == 0):
        return None
    elif (length == 1):
        return 1
    elif (length % 2 == 0):
        return length // 2
    else:
        return (length // 2) + 1

def get_median(x):
    '''
    Gets the median of a sorted list x
    '''
    length = len(x)
    if (length == 0):
        return None
    elif (length % 2 == 0):
        return (x[length // 2] + x[(length // 2) - 1])/2
    else:
        return x[length // 2]
