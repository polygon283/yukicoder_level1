L = int(input()) #箱の幅
N = int(input()) #ブロックの個数←使わなかった
W = list(map(int,input().split())) #ブロックの幅

W.sort()
def max_block(L,W):
    count = 0
    current_L = 0

    for brock in W:
        if current_L + brock <= L:
            current_L += brock
            count += 1
        else:
            break
    return count

print(max_block(L,W))