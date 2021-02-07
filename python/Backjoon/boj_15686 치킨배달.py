import sys
import itertools

read = sys.stdin.readline
N, M = map(int,read().split())

mat,houses,chicken_houses = [],[],[]

for i in range(N):
    a = list(map(int,read().split()))
    for j in range(N):
        if a[j] == 2:
            chicken_houses.append((i,j))
        elif a[j] == 1:
            houses.append((i,j))

def combinations(arr,r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in combinations(arr[i+1:],r-1):
                yield next + [arr[i]]
def L1_distance(A,B):
    return abs(A[0]-B[0]) + abs(A[1]-B[1])

sol = []
for choose_chicken_houses in combinations(chicken_houses,M):
    city_distance = 0
    for house in houses:
        dist = 1000 # > 최대거리 100
        for chicken_house in choose_chicken_houses:
            dist = min(dist,L1_distance(house,chicken_house))
        city_distance += dist
    sol.append(city_distance)

print(min(sol))


