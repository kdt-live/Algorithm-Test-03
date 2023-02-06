# 괄호 짝짓기

import sys
sys.stdin = open("input_1218.txt")
input = sys.stdin.readline

for T in range(10):
    input()
    string = input().strip()
    s = sorted(set(string))
    result = {x: [] for x in s[::2]}
    d = dict(zip(s[1::2], s[::2]))    
    for j in string:
        if j in result.keys():
            result[j] += [j]
        else:
            try:
                result[d.get(j)].pop()
            except:
                break

    r = []
    for i in result.values():
        r += i

    if r:
        print(f"#{T + 1} 1")
    else:
        print(f"#{T + 1} 0")