T = int(input())

for test_case in range(1,T+1):
    a, b = map(int,input().split())

    numbers = list(map(int,input().split()))

    nobody = []

    for i in range(1,a+1):
        if i not in numbers:
            nobody.append(i)

    print('#{}'.format(test_case),*nobody)
