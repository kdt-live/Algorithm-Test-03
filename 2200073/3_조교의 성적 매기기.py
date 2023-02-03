import sys
sys.stdin = open('input_3.txt', 'r')

# 미완성
s = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
T = int(input())
for t in range(T):
    n, k = map(int, input().split())
    d = [sum(map(int, input().split())) for _ in range(n)]
    target = d[k-1]
    d = sorted(d,reverse=True)
    rank = d.index(target)+1
    p = (d.index(target)+1)/(n//10)
    # d_ = sorted(d)
    # rank_ = d.index(target)+1
    # nn = n//10
    # if rank % nn == 0:
    #     r = rank//nn -1
    # else:
    #     r = rank//nn
    
    
    
    # nn = (n//10)
    # r = -(-(d.index(target)+1))//(n//10)

    print(f'#{t+1}',rank,n,f'{p:.3}')
    # print(f'#{t+1}',rank_,n)
    # print(s[r])