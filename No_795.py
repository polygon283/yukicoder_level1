import sys

sys.set_int_max_str_digits(51000) #REを回避できた

N = int(input())
M = int(input())


total = 10*N + M

if N % 2 == 0 and M % 2 == 0:
    print("Yes")
elif M % 10 == 0:
    if total % 2 == 0:
        print("Yes")
else:
    print("No")
