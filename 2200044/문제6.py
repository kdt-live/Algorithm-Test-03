T = int(input())
for i in range(T):
    switch1 = 0
    switch2 = 0
    sum = 0
    d = []
    e = []
    a, b = map(int,input().split())
    arr = [[0 for _ in range(a)] for _ in range(a)]
    for j in range(a):
        c = list(map(int,input().split()))
        for k in range(a):
            arr[j][k] = c[k]
    for l in range(a):
        for m in range(a):
                    if arr[l][m] == 0 and switch2 == 0:
                        switch1 = 0
                    elif arr[l][m] == 0 and switch2 == 1:
                        d.append(sum)
                        sum = 0
                        switch1 = 0
                        switch2 = 0
                    elif arr[l][m] == 1 and switch1 == 0:
                        if m != a-1:
                            sum += 1
                            switch1 = 1
                            switch2 = 1
                        else: 
                            sum += 1
                            d.append(sum)
                            sum = 0
                    elif arr[l][m] == 1 and switch1 == 1:
                        if m != a-1:
                            sum += 1
                            switch2 = 1
                        else:
                            sum += 1
                            d.append(sum)
                            sum = 0
        switch1 = 0
        switch2 = 0
        sum = 0
    for n in range(a):
        for o in range(a):
                if arr[o][n] == 0 and switch2 == 0:
                    switch1 = 0
                elif arr[o][n] == 0 and switch2 == 1:
                    e.append(sum)
                    sum = 0
                    switch1 = 0
                    switch2 = 0
                elif arr[o][n] == 1 and switch1 == 0:
                    if o != a-1:
                        sum += 1
                        switch1 = 1
                        switch2 = 1
                    else:
                        sum += 1
                        e.append(sum)
                        sum = 0
                elif arr[o][n] == 1 and switch1 == 1:
                    if o != a-1:
                         sum += 1
                         switch2 = 1
                    else:
                         sum += 1
                         e.append(sum)
                         sum = 0
        switch1 = 0
        switch2 = 0
        sum = 0
    print(f"#{i+1} {d.count(b) + e.count(b)}")