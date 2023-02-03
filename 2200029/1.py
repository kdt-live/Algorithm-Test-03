import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())

for t in range(1, T + 1):
    N, K = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    all = list(range(1, N + 1))
    for num in nums:
        if num in all:
            all.remove(num)
    print(f'#{t}', *all)