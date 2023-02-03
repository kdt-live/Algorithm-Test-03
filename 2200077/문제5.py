# 암호 생성기
# 미완성
T = int(input())

for t in range(T):
    numbers = list(map(int, input().split()))

    for i in range(1, 6):
        numbers.append(numbers.pop(0) - i)
    print(numbers)

