def compress(s,length,ret_s):
    while 2*length <= len(s):
        sub, k = s[:length], 1
        while sub == s[k*length:(k+1)*length]:
            k += 1
        if k != 1:
            ret_s += str(k)+sub
            s = s[k*length:]
        else:
            ret_s += s[:length]
            s = s[length:]
    ret_s += s
    return len(ret_s)

def solution(s):
    return min([compress(s,i,'') for i in range(1,(len(s)//2) +1)]) if len(s) != 1 else 1