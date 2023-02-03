import sys
sys.stdin = open('input_4.txt', 'r')

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
                        else:
                            j += k
                            while j < n:
                                if i[j] == 1:
                                    j += 1
                                else:
                                    break
            j += 1
    d_ = list(zip(*d))
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
                            cnt += 1
                        elif i[a+1] == 0:
                            cnt += 1
                            j += k
                        else:
                            j += k
                            while j < n:
                                if i[j] == 1:
                                    j += 1
                                else:
                                    break
            j += 1
    print(f'#{t+1} {cnt}')