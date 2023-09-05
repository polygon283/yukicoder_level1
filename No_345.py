def min_chiwawa_length(s):
    min_len = len(s) + 1
    
    
    for i in range(len(s)):
        if s[i] == 'c':

            first_w = s.find('w',i)
            if first_w == -1:
                break
            second_w = s.find('w',first_w + 1)
            if second_w == -1:
                break

        length = second_w - i + 1
        min_len = min(min_len,length)

    if min_len == len(s) + 1:
        return -1
    else:
        return min_len
s = input()
print(min_chiwawa_length(s))
