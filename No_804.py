input_list = input().split()

A = int(input_list[0])
B = int(input_list[1])
C = int(input_list[2])
D = int(input_list[3])

def max_veg_count(A,B,C,D):
    for x in range(A, -1, -1):
        if x*C <= B and x + x*C <= D:
            return x
        
    return 0
        
print(max_veg_count(A,B,C,D))
    


