import sys
sys.stdin = open('2200053/input.txt')

T = int(input())

for t in range(1, T+1):
    N, K = map(int, input().split())
    K_number = list(map(int, input().split()))
    #print(N, K)
    #print(K_number)
    
    #print(max(N))
    n_list = []
    
    for n in range(1, N+1):
        #print(n)
        if n not in K_number:
            n_list.append(n)
    n_list.sort()
    #print(str(n_list)[1:-1].replace(',', ''))
    a = str(n_list)[1:-1].replace(',', '')
    print(f'#{t} {a}')
