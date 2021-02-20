# 집합은 순서에 상관 없으므로 원소의갯수가 작은 집합부터 순서대로 찾아가면 됨.
# 1. sort by len(sub_s) sub_s in s
# 2. 한개씩 줄여나감.
def solution(s):
    s,check = s[2:-2].split('},{'), {}
    for sub_s in sorted(s, key=lambda x : len(x)):
        sub_s = sub_s.split(',')
        if len(check) == 0:
            check[sub_s[0]], answer = 1, [int(sub_s[0])]
        else:
            for m in sub_s:
                if m not in check:
                    answer.append(int(m))
                    check[m] = 1
    return answer