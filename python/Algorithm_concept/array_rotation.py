arr = [ [1,1,1,1,1],
        [0,3,4,5,0],
        [1,2,1,6,1],
        [0,9,8,7,0],
        [1,1,1,1,1] ]

def array_rotation_anticlock(arr):
    return list(reversed(list(map(list,zip(*arr)))))
def array_rotation_clock(arr):
    return list(map(list,map(reversed,zip(*arr))))

arr = array_rotation_clock(arr)
for a in arr:
    print(a)
print()

arr = array_rotation_anticlock(arr)
for a in arr:
    print(a)
print()

