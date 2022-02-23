ar = [1,2,3,4,5]

def combinations(arr,r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in combinations(arr[i+1:],r-1):
                yield [arr[i]] + next

for com in combinations(ar,3):
    print(com)