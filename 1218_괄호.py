import sys

sys.stdin = open('input.txt')

for i in range(1, 11) :
    n = int(input())
    string = input()

    if n%2 == 0 :
        for _ in range(n//2) :
            string = string.replace('()','')
            string = string.replace('{}','')
            string = string.replace('<>','')
            string = string.replace('[]','')

        if len(string) == 0 :
            print(f'#{i} 1')
        else :
            print(f'#{i} 0') 
    else   :         
        print(f'#{i} 0') 