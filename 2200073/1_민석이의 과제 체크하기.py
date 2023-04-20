import sys
sys.stdin = open('input_1.txt', 'r')

import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):
    n, k = map(int, input().split())
    d = list(map(int, input().split()))
    
    r = [i for i in range(1, n+1) if i not in d]
    print(f'#{t+1}', *r)