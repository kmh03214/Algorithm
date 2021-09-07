# 10*1 이상의 차이가 안날 것이므로, 자릿수에 점수를 부여한다.

import sys
read = sys.stdin.readline
N = int(read())
words, wordmap, priority = [], {}, {}

for i in range(N):
    word = read()[:-1]
    idx = 1
    for c in word:
        if c not in priority:
            priority[c] = 10**(len(word)-idx)
        else:
            priority[c] += 10**(len(word)-idx)
        idx+=1
    words.append(word)
num = 9
for c in sorted(priority.keys(), key = lambda x : priority[x], reverse= True):
    wordmap[c] = num
    num -= 1
sol = []
for word in words:
    sol.append(''.join([ str(wordmap[w]) for w in word]))
ss = 0
for s in sol:
    ss += int(s)
print(ss)
