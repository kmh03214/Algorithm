T = int(input())


for test in range(1,T+1):
    sol = 1
    N,M = map(int,input().split())
    arr = [2**i for i in map(int,input().split())]
    arr.sort(reverse = True)

    remain_tile = [(M,M)] # (w,h)
    # 큰거부터
    while arr:
        Next = []
        Next_remain = []
        for tile in arr:
            a = tile
            for w,h in remain_tile:
                if a <= w and a <= h:
                    remain_tile.remove((w,h))
                    arr.remove(tile)
                    if w-a != 0:
                        remain_tile.append((w-a,a))
                    if h-a != 0:
                        remain_tile.append((w,h-a))
                else:
                    Next_remain.append((w,h))

                    remain_tile.append((M-a,a))
                    remain_tile.append((M,M-a))
                    sol += 1
                    continue

    print("#%d %d"%(test,sol))

