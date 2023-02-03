

T = int(input())
for t in range(1, T+1):
        a, b = map(int, input().split())
        submit = list(map(int, input().split()))
        result = []
        for i in range(1, a+1):
            if i not in submit:
                result.append(i)
        print(f'#{t}', *result)