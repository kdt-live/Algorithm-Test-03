import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

test = int(input())

for i in range(test):
    n, m = map(int, input().split())
    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().split())))

    # 잡을 수 있는 파리 최대값을 저장할 변수
    ans = 0
    # 순회하면서 범위 안에 있는 파리 수를 저장할 변수
    tmp = 0

    # 전체 리스트를 파리채 크기씩 끊어서 순회할거라 range를 조정
    for a in range(n - m + 1):
        for b in range(n - m + 1):
            for c in range(m):
                for d in range(m):
                    tmp += arr[a+c][b+d]

            ans = max(ans, tmp)
            tmp = 0

    print(f"#{i+1} {ans}")