def powerset(s):
    masks = [1 << i for i in range(len(s))] # 마스크 생성 1,10,100,1000...
    for i in range(1<<len(s)): # 총 1<<s 즉 2**s개 부분집합 생성
        yield [ss for ss,mask in zip(s,masks) if mask&i]

for subset in powerset([1,2,3,4,5]):
    print(subset)



def powerset(s):
    masks = [1 << i for i in range(len(s))]
    for i in range( 1 << len(s)):
        yield [ss for ss,mask in zip(s,masks) if i & mask]

for power in powerset([1,2,3,4,5]):
    print(power)
