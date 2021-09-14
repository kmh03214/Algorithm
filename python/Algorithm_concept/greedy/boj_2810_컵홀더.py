N = int(input())
seats = input()

holder, sol, jump = 1, 0, 0
for s in seats:
    if s == 'S':
        continue
    else:
        if jump:
            jump = 0
            continue
        jump = 1
        if holder == 0:
            sol += 1
        else:
            holder -= 1

print(len(seats)-sol)

# n = input()
# s = input()
# if "LL" in s:
# 	ret = s.replace("LL","C")
# 	print(len(ret)+1)
# else:
# 	print(len(s))
