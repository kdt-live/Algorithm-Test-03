import sys
# sys.stdin = open('input_4.txt', 'r')
sys.stdin = open('2200073/input_4.txt', 'r')

# 미완성
T = int(input())
for t in range(T):
    n, k = map(int, input().split())
    d = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0
    for i in d:
        j = 0
        while j < n: 
            if i[j] == 1:
                if j < n-k+1:
                    for a in range(j, j+k):
                        if i[a] != 1:
                            break
                    else:
                        if j == n-k:
                            cnt += 1
                        elif i[a+1] == 0:
                            cnt += 1
                    j += k
                    while j < n:
                        if i[j] == 0:
                            break
                        else:
                            j += 1
            j += 1
    d_ = list(zip(*d))
    cnt2 = 0
    for i in d_:
        j = 0
        while j < n: 
            if i[j] == 1:
                if j < n-k+1:
                    for a in range(j, j+k):
                        if i[a] != 1:
                            break
                    else:
                        if j == n-k:
                            cnt2 += 1
                        elif i[a+1] == 0:
                            cnt2 += 1
                    j += k
                    while j < n:
                        if i[j] == 0:
                            break
                        else:
                            j += 1
            j += 1
    print(cnt,cnt2)