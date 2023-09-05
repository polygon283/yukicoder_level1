N = int(input())
M = int(input())
total = 100*N + 10*M

if N % 2 == 0 and M % 2 == 0:
    print("Yes")
elif M % 10 == 0:
    if total % 2 == 0:
        print("Yes")
else:
    print("No")
#REになってしまう