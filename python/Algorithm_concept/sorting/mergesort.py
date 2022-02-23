arr = [1,5,2,3,4,6,2,1,0]

def index_sort(arr1,arr2):
    ret = []
    idx1 , idx2 = 0, 0
    while idx1 < len(arr1) or idx2 < len(arr2):
        if idx1 >= len(arr1):
            ret.append(arr2[idx2])
            idx2 += 1
            continue

        if idx2 >= len(arr2):
            ret.append(arr1[idx1])
            idx1 += 1
            continue

        if arr1[idx1] < arr2[idx2]:
            ret.append(arr1[idx1])
            idx1 += 1
        
        else:
            ret.append(arr2[idx2])
            idx2 += 1

    return ret



def merge_sort(s,e):
    if s == e:
        return [arr[s]]
    
    if s < e//2:
        a1 = merge_sort(s, e//2 )
    else:
        a1 = []
    if e > (e//2) + 1:
        a2 = merge_sort((e//2)+1,e)
    else:
        a2 = []
    print(a1,a2)
    return index_sort(a1,a2)

sorting_arr = merge_sort(0,len(arr)-1)
print(sorting_arr)