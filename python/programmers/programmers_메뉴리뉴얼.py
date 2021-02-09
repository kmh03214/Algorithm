from itertools import combinations

def choose_menu(order,r):
    return combinations(order,r)

def solution(orders, course):
    answer = {}
    for i in range(len(orders)):
        order = orders[i]

        for course_num in course:
            combi = choose_menu(sorted(order),course_num)
            max_order_num = 0
            nomi = []
            for com in combi:
                com = ''.join(com)
                order_num = 0
                
                for j in range(len(orders)):

                    exist = 1
                    for menu in com:
                        if menu not in orders[j]:
                            exist = 0
                            break
                    if exist:
                        order_num += 1

                if order_num > 1 and order_num > max_order_num:
                    max_order_num = order_num
                    nomi = [(com,order_num)]
                elif order_num > 1 and order_num == max_order_num:
                    nomi.append((com,order_num))

            if nomi:
                for nom, cnt in nomi:
                    nom = ''.join(sorted(nom))

                    if course_num not in answer:
                        answer[course_num] = [(nom,max_order_num)]
                    else:
                        if answer[course_num][0][1] < max_order_num:
                            answer[course_num] = [(nom,max_order_num)]
                        elif answer[course_num][0][1] == max_order_num:
                            if (nom,max_order_num) not in answer[course_num]:
                                answer[course_num].append((nom,max_order_num))
    ans = []
    for val in answer.values():
        for v in val:
            ans.append(v[0])
    ans.sort()
    return ans



# import collections
# import itertools

# def solution(orders, course):
#     result = []

#     for course_size in course:
#         order_combinations = []
#         for order in orders:
#             order_combinations += itertools.combinations(sorted(order), course_size)

#         most_ordered = collections.Counter(order_combinations).most_common()
#         result += [ k for k, v in most_ordered if v > 1 and v == most_ordered[0][1] ]

#     return [ ''.join(v) for v in sorted(result) ]