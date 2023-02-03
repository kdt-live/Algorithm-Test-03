def password_maker(list):
    while True:
        for i in range(1, 6):
            number = list.pop(0)
            list.append(number - i)

            if list[-1] <= 0:
                list[-1] = 0
                return list

for i in range(1, 11):
    tc = int(input())
    numbers = list(map(int, input().split()))

    result = password_maker(numbers)
    print('#{}'.format(tc), *result)