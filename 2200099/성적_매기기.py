import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for t in range(1, T+1):
    tmp = []
    N, k = list(map(int, input().split()))
    for n in range(N):
        a, b, c = list(map(int, input().split()))
        tmp.append(a*0.35 + b*0.45 + c*0.20)
    tmp.sort(reverse= True)
    print(tmp)
