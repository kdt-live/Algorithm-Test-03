import sys
sys.stdin = open('input_3.txt', 'r')

s = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
T = int(input())
for t in range(T):
    n, k = map(int, input().split())
    d = [list(map(int, input().split())) for _ in range(n)]

    # 점수 비중이 다른것을 모르고 삽질하다가 시간을 많이 썼다...
    d_ = [(i[0]*35 + i[1]*45 + i[2]*20)/100 for i in d]

    target = d_[k-1]
    d_ = sorted(d_,reverse=True)
    rank = d_.index(target) + 1
    g = -(-rank//(n//10)) - 1

    print(f'#{t+1}', s[g])