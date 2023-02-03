import sys
sys.stdin = open("input.txt", "r")

def space_finder(space):
    empty_space = 0
    for ls in space:
        cnt = 0
        for j in range(len(ls)):
            if ls[j]:
                cnt += 1
            else:
                if cnt == k:
                    empty_space += 1
                cnt = 0
    return empty_space

T = int(input())
for t in range(1, T+1):
    n, k = map(int,input().split())
    space = [list(map(int,input().split())) + [0] for _ in range(n)] + [[0]*(n+1)]
    space_zip = list(map(list,zip(*space)))

    answer = space_finder(space) + space_finder(space_zip)
    print(f'#{t} {answer}')