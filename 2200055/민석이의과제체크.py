#민석이의 과제체크
import sys
input=sys.stdin.readline
T=int(input())
for i in range (1,T+1):
    N,K=map(int,input().split())
    all_student=set(range(1,N+1))
    submit=set(map(int,input().split()))
    ans=list(all_student-submit)
    print(f'#{i}',end=' ')
    print(*ans)