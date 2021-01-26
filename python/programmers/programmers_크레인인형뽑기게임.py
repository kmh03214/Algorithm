def solution(board, moves):
    q, N,check, answer = [], len(board), {}, 0 
    # moves의 하나를 인자로 받아 board에서 꺼내는 함수 (m = move-1 idx)
    def choose(m):
        if check[m-1] != N:
            doll = board[check[m-1]][m-1]
            check[m-1] += 1
            return doll
        else: # 끝까지 탐색해서 비어있는상태
            return 0
        
    for i in range(N):
        for j in range(N):
            if board[j][i] != 0:
                check[i] = j # i번째 칸의 높이는 j다.
                break
    for m in moves:
        doll = choose(m)
        if doll:
            if not q:
                q.append(doll)
            else:
                if q[-1] == doll:
                    q.pop()
                    answer += 2
                else:
                    q.append(doll)
    return answer