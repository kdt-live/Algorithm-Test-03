'''1_5431민석이의 과제 체크하기 D3

수강생들은 1번에서 N번까지 
과제를 제출하지 않은 사람의 번호를 오름차순으로 출력
[입력]

첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 수강생의 수를 나타내는 정수 N(2≤N≤100)과 
과제를 제출한 사람의 수를 나타내는 정수 K(1≤K≤N)가 공백으로 구분되어 주어진다.

두 번째 줄에는 과제를 제출한 사람의 번호 K개가 공백으로 구분되어 주어진다. 

[출력]
각 테스트 케이스마다 과제를 제출하지 않은 사람의 번호를 오름차순으로 출력한다.'''

import sys
sys.stdin = open("input.txt", "r")
import heapq

T = int(input())
lst = []
for test_case in range(1, T+1):
    N, K = map(int,input().split())
    k = list(map(int, input().split()))
    for n in range(1, N+1):
        if n not in k:
            heapq.heappush(lst,n)
    print(f'#{test_case}',*lst)
    lst.clear()
