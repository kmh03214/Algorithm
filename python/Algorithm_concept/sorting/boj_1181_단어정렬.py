import sys
read = sys.stdin.readline
N = int(read())
[print(word, end = '') for word in sorted(set([read() for i in range(N)]), key = lambda x : (len(x),x)) ]