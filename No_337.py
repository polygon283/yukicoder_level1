input_string = input()
split_string = input_string.split()

N = int(split_string[0])
P = int(split_string[1])

def p_vs_np(N,P):
    if P == N * P:
        return '='
    else:
        return '!='
    
if -50 <= N <= 50 and -50 <= P <= 50:
    print(p_vs_np(N,P))