def find_road_number(S): #現在の交差点を計算する関数
    road_number = 1
    
    for junction in S: 
       
        if junction == "L":
            road_number = road_number * 2
        elif junction == "R":
            road_number = road_number * 2 + 1
    
    return road_number

S = input()
print(find_road_number(S))
