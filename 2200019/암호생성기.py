for _ in range(10):
    n = int(input())
    n_list = list(map(int,input().split()))
    while True:
        if n_list[7] <= 0:
             print(f'#{n}',*n_list[:7],0)
             break
        else:
            n_list.append((n_list.pop(0)-1))
            
        if n_list[7] <= 0:
            print(f'#{n}',*n_list[:7],0)
            break
        else:
            n_list.append((n_list.pop(0)-2))
            
        if n_list[7] <= 0:
            print(f'#{n}',*n_list[:7],0)
            break
        else:
            n_list.append((n_list.pop(0)-3))
            
        if n_list[7] <= 0:
            print(f'#{n}',*n_list[:7],0)
            break
        else:
            n_list.append((n_list.pop(0)-4))

        if n_list[7] <= 0:
            print(f'#{n}',*n_list[:7],0)
            break
        else:
            n_list.append((n_list.pop(0)-5))
