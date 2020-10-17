test = int(input())

for t in range(test):
    N, submit_num = map(int,input().split())
    students = { i+1 : 1 for i in range(N)}
    submit_students = list(map(int,input().split()))
    for i in range(submit_num):
        if submit_students[i] in students:
            del students[submit_students[i]]
    sol = sorted(list(students.keys()))
    print("#%d "%(t+1), end ='')
    for s in sol:
        print(s, end = ' ')
    print()