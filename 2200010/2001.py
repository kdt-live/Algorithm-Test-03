# 2001번 파리퇴치

'''
N x N 배열 안의 숫자는 해당 영역에 존재하는 파리의 개수를 의미한다.
M x M 크기의 파리채를 한 번 내리쳐 최대한 많은 파리를 죽이고자 한다.
죽은 파리의 개수를 구하라!

<제약 사항>
1. 5<= N <= 15
2. 2<= M <= 15
3. 각 영역 파리 개수 <= 30
'''

# import sys
# sys.stdin = open('data/2001.txt')

# T = int(input())

# for t in range(1, T + 1):
N, M = list(map(int, input().split()))
square = [list(map(int, input().split)) for _ in range(N)]

        # 최대한 많이 죽인 파리의 개수(max)
        # 델타 탐색

for i in range(N):
    for j in range(N):
        # 더이상 가지 않아도 될 때 break를 걸자
        # break 범위: N-1일 때 break 즉 n-2까지만 가도록하게 만들자.

        # M 값의 범위
        pass

