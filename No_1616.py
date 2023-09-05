def sum_divisors(N):
    sum_divisors = 0
    for i in range(1,N + 1):
        if N % i == 0:
            sum_divisors += i
    return sum_divisors

N = int(input())

if 1 <= N <= 100:
    A = sum_divisors(N)
    B = A / N

    print(int(A / B))

