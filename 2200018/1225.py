# 암호생성기
import sys
sys.stdin = open("input_1225.txt")
input = sys.stdin.readline

from itertools import cycle

while True:
    try:
        T = input().strip()
        ls = list(map(int, input().split()))
        for i in cycle(range(1, 6)):
            n = ls[0] - i 
            if  n <= 0:
                n = 0
                ls = ls[1:] + [n]
                break
            else:
                ls = ls[1:] + [n]

        print(f"#{T}:", *ls)

    except:
        break