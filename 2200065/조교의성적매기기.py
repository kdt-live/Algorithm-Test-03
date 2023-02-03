import sys
sys.stdin = open("input3.txt", "r")

for i in range(1,int(input())+1):
    n,m = map(int,input().split())
    grade = ['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']
    score = {}
    for j in range(1,n+1):
        a,b,c = map(int,input().split())
        lst = [a*0.35,b*0.45,c*0.2]
        score[j]= sum(lst)
    new_score = sorted(score.items(),key=lambda x:x[1], reverse=True)
    for num in new_score:
        if num[0] == m:
            print(f'#{i}',grade[(new_score.index(num))//(n//10)])