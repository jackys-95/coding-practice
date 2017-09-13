def max_span(a):
    '''
    a is a list of ints
    '''
    int_map = {}
    for i in range(len(a)):
        if a[i] not in int_map:
            int_map[a[i]] = [i]
        else:
            if len(int_map[a[i]]) == 1:
                int_map[a[i]].append(i)
            else:
                int_map[a[i]][1] = i
    maximum_span = -1
    for item in int_map.values():
        span_value = 0
        if len(item) == 1:
            span_value = 1
        else:
            span_value = item[1] - item[0] + 1
        if span_value > maximum_span:
            maximum_span = span_value
    return maximum_span

print(max_span([1, 2, 1, 1, 3]))
print(max_span([1, 4, 2, 1, 4, 1, 4]))
print(max_span([1, 4, 2, 1, 4, 4, 4]))
