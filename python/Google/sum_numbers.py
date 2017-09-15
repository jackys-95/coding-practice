def sum_numbers(x):
    '''
    x is a string, search for all numbers and sum them
    '''
    total = 0
    current_num = ""
    for char in x:
        if char.isdigit():
            current_num += char
        else:
            if current_num:
                total += int(current_num)
                current_num = ""
    current_num = 0 if not current_num else current_num
    return total + int(current_num) # case where num was @ end of string

print(sum_numbers("abc123xyz"))
print(sum_numbers("aa11b33"))
print(sum_numbers("7 11"))
