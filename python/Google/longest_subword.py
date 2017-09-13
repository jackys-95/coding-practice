def find_longest_subword(s, d):
    '''
    s is string
    d is the collection of words
    returns the longest subsequene word
    '''
    max_word = ["", 0]
    s_len = len(s)
    for item in d:
        item_len = len(item)
        if item_len > s_len:
            continue
        i = 0
        j = 0
        valid = False
        while i < item_len and j < s_len:
            if item[i] == s[j]:
                i += 1
                valid = True
            else:
                j += 1
                valid = False
        if valid and item_len > max_word[1]:
            max_word[0] = item
            max_word[1] = item_len
    return max_word[0]
