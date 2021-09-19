numbers = list(map(int,' '.join(input()).split()))
if sum(numbers[:len(numbers)//2]) == sum(numbers[len(numbers)//2:]):
    print('LUCKY')
else:
    print('READY')