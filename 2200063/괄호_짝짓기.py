import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

for _ in range(10):
    T = int(input())
    S = input()
    result = {}
    res = 0
    for i in (S):
        if i in result:
            result[i] += 1
        else:
            result[i] = 1

    if result['('] == result[')'] and result['['] == result[']'] and result['{'] == result['}'] and result['<'] == result['>']:
        res = 1
        print(f'#{_+1} {res}')
    else:
        print(f'#{_+1} {res}')