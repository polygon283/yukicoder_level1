N = input()

def Digit_Sum_Sequence(N): #a100を求める関数
    for _ in range(100):
        sum = 0
        for Digit in str(N):
            sum += int(Digit)
        N = sum
    return N

print(Digit_Sum_Sequence(N))