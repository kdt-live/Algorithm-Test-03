T = int(input())

for test_case in range(1, T+1):
    a, b = map(int,input().split())

    squ = [list(map(int,input().split())) for _ in range(a)]

    fly = []

    for i in range(a-b+1):
        for j in range(a-b+1):
            total = 0

            for ai in range(b):
                for aj in range(b):
                    if i + ai in range(a) and j + aj in range(b):
                        total += squ[i + ai][j + aj]

                fly.append(total)

max = fly[0]
for i in fly:
    if i > max:
        max = i

print('#{} {}'. format(test_case, max))