
for i in range(1,11):
    n = int(input())
    n_s = str(input())
    for _ in range(n//2):
        if '()' in n_s :
            n_s = n_s.replace('()','')
        elif '[]' in n_s :
            n_s = n_s.replace('[]','')
        elif '{}' in n_s :
            n_s = n_s.replace('{}','')
        elif  '<>' in n_s :
            n_s = n_s.replace('<>','')
        else:
            if len(n_s) == 0:
                print(f'#{i} 1')
                break
    if len(n_s) != 0:
        print(f'#{i} 0')


