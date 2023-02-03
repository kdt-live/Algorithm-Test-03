''' 2001 파리퇴치
N x N 배열 안의 숫자는 해당 영역에 존재하는 파리의 개수를 의미한다.
[제약 사항]
1. N 은 5 이상 15 이하이다.
2. M은 2 이상 N 이하이다.
3. 각 영역의 파리 갯수는 30 이하 이다.
[입력]
가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
각 테스트 케이스의 첫 번째 줄에 N 과 M 이 주어지고,
다음 N 줄에 걸쳐 N x N 배열이 주어진다.
[출력]
출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)'''

import sys
sys.stdin = open("input.txt", "r")
from pprint import pprint
from collections import ChainMap
from itertools import combinations


T = int(input())
for test_case in range(1, T+1):
    N, K = map(int,input().split())
    matrix = [ list(map(int, input().split())) for _ in range(N)] 
    dx = [0, 1, 0, -1]
    dy = [0, 0, 1, 0]
    print('===============')
    pprint(matrix)
    lst = []
    for x  in range(N):
        for y  in range(N):
            print(x, y)
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < N and 0 <= ny < N:
                    x = nx
                    y = ny
                    lst.append(matrix[x][y])
                    if len(lst) == 4:
                        print(sum(lst),lst)
                        print(x, y, matrix[x][y])
                        print()
                        lst = []