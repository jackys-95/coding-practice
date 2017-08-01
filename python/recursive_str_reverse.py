def recursive_str_reverse(x):
    if (len(x) < 1):
        return x
    else:
        return recursive_str_reverse(x[1:]) + x[0] 
