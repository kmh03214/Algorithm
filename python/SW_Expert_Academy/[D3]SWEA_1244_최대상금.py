T = int(input())
def combinations(arr,r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in combinations(arr[i+1:],r-1):
                yield next + [arr[i]]

def swap_case(arr): # idx에 따라 스왑된 모든 arr 경우를 순차적으로 리턴
    idxs = [i for i in range(len(arr))]
    for com in combinations(idxs,2):
        ret = arr.copy()
        ret[com[0]],ret[com[1]] = ret[com[1]],ret[com[0]]
        yield ret
    
def swap(arr,r):
    if r == 0:
        yield arr
    else:
        for i in range(r):
            for ret in swap_case(arr): # ret 은 arr
                for sol in swap(ret,r-1):
                    yield sol

for test in range(T):
    numbers, swap_n = map(int,input().split())
    numbers = ' '.join(str(numbers)).split() # numbers는 char list
    max_num = ''.join(sorted(numbers,reverse =True))
    sols, flag = ['0'] ,(swap_n-5)

    for nomi in swap(numbers,min(swap_n,5)):
        sol = ''.join(nomi)
        if sol == max_num:
            sols[0] = sol
            break
        if sols[0] < sol:
            sols[0] = sol
    
    if flag > 0:
        if flag % 2 == 0:
            print('#%d'%(test+1),max(sols))
        else:
            s = ' '.join(max(sols)).split()
            s[-1],s[-2] = s[-2],s[-1]
            print('#%d'%(test+1),''.join(s) )
    else:
        print('#%d'%(test+1),max(sols))
