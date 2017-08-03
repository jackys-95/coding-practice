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
            median = get_median(a.append(b[0]))
        elif (median_a > median_b):
            median = two_sorted_arrays_median(a[0:calculate_slice_index(length_a)], \
                                              b[calculate_slice_index(length_b):])
        else:
            median = two_sorted_arrays_median(b[0:calculate_slice_index(length_b)], \
                                              a[calculate_slice_index(length_a):])
    return median

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
        return (x[length // 2] + x[(length//2) - 1])/2
    else:
        return x[length // 2]
