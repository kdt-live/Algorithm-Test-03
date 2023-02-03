'''
민석이의 과제 체크하기
'''

# import sys
# sys.stdin = open('6.txt', 'r')

t = int(input())

for _ in range(1, t+1):
    n,k = map(int,input().split())
    data = list(map(int, input().split()))
    result = []

    for i in range(1, n+1):
        if i not in data:
            result.append(i)
    print(f'#{_}', *result)
