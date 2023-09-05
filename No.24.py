N = int(input())
number_set = set(range(10))

if 2 <= N <= 6:
    for i in range(N):
        *numbers, answer = input().split()
        numbers = set([int(num) for num in numbers])

        if answer == "NO":
            number_set -= numbers
        elif answer == "YES":
            number_set &= numbers
                

print(number_set.pop())
                        
        
