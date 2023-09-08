N = int(input()) 

def count_conbination(N): 
    count = 0
    max_T = N // 5 

    for T in range(max_T + 1):
        for C in range(T + 1):
            TC_sum = (5*T + 2*C)
            if (N - TC_sum) % 3 == 0 and (N - TC_sum) >= 0:
                count += 1
    
    return count

print(count_conbination(N))