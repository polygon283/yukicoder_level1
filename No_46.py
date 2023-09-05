def steps(a,b):
    result = b // a
    if b % a != 0:
        return result +1
    else:
        return result
    
input_string = input()
split_string = input_string.split()

a = int(split_string[0])
b = int(split_string[1])
print(steps(a,b))

