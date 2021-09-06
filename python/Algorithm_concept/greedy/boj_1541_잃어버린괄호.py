polynomial_list = input().split('-')

print(sum(map(int,polynomial_list[0].split('+'))) -  sum([sum(map(int, poly.split('+'))) for poly in polynomial_list[1:]]))
