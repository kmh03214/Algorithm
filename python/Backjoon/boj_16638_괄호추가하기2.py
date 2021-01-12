import sys
read = sys.stdin.readline
N = int(read())
EXP = ' ' + ' '.join(read())
sol = []
def cal(exp):
    d = {'+':1 , '*':1 , '-':1}
    s,fg = 0,0
    for i in range(len(exp)):
        if fg == 1:
            if exp[i] == ')':
                if s >= 2:
                    return 0
                fg,s = 0, 0

        if exp[i] == '(':
            fg = 1
        else:
            if fg == 1 and exp[i] in d:
                s += 1
            continue
    return 1

def dfs(cnt,flag, prefix, exp):
    # 종료조건
    if cnt == 2*N+1:
        # print("cnt:",cnt)
        try:
            if cal(prefix):
                    sol.append(eval(prefix))
                #print(prefix)
            # else:
                #print("이건안돼:",prefix)
            return
        except:
            return
    
    if flag == 0:
        if cnt%4 == 0:
            flag = 1 # 좌측괄호 함
            dfs(cnt+1, flag, prefix + '(', exp)
            flag = 0 
            # if len(prefix) == 0 or prefix[-1] == '+' or prefix[-1] == '*' or prefix[-1] == '-' : 
            #     dfs(cnt+1, flag, prefix , exp) # 아무것도 안하고 넘어감
            # else:
            #     dfs(cnt+1, flag, prefix + exp[cnt], exp) # 아무것도 안하고 넘어감
        else:
            if len(prefix) == 0 or prefix[-1] == '+' or prefix[-1] == '*' or prefix[-1] == '-': 
                dfs(cnt+1, flag, prefix , exp) # 아무것도 안하고 넘어감
            else:
                dfs(cnt+1, flag, prefix + exp[cnt], exp) # 아무것도 안하고 넘어감
    else:
        if cnt%4 == 2:
            flag = 0 # 우측괄호 닫음
            # print("abc",cnt,len(prefix))
            dfs(cnt+1, flag, prefix + exp[len(prefix):cnt]+')' + exp[cnt+1] , exp)
            # print("def",cnt,len(prefix))
            flag = 1
            dfs(cnt+1, flag, prefix + exp[cnt], exp) # 아무것도 안하고 넘어감
        else:
            dfs(cnt+1, flag, prefix + exp[cnt], exp) # 아무것도 안하고 넘어감

dfs(0,0,'',EXP)
print(max(sol))