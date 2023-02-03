import sys
sys.stdin = open("input.txt", "r")

for t in range(1,int(input())+1):
    n,m= map(int,input().split())
    fly =[list(map(int,input().split()))for _ in range(n)]
    many_die = 0
    for x in range(n-(m-1)):
        for y in range(n-(m-1)):
            die = 0
            for i in range(m):
                for j in range(m):
                    die += fly[x+i][y+j]
            many_die=max(many_die,die)    
    print(f'#{t}', many_die)