S = input()
bef = S[0]
cnt = {'0':0,'1':0}
for s in S:
    if s != bef:
        cnt[bef] += 1
        bef = s
cnt[s] += 1
print(cnt[min(cnt, key = lambda x : cnt[x])])
