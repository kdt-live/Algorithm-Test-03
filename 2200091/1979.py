import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

test = int(input())

for i in range(test):
    n, l = map(int, input().split())
    puzzle = []
    # 행에서 빈칸을 카운하는 변수, 열에서 빈칸을 카운트하는 변수, 단어가 들어갈 수 있는 자리를 카운트하는 변수
    r_cnt = c_cnt = res = 0

    for _ in range(n):
        puzzle.append(list(map(int, input().split())))

    # 행 검사
    for a in range(n):
        r_cnt = 0
        for b in range(n):
            # 검은 부분을 만나면
            if puzzle[a][b] == 0:
                # 지금까지 카운트한 빈칸과 단어 길이를 비교
                # 같으면 res에 +1, 아니면 r_cnt 값을 0으로 바꿈
                if r_cnt == l:
                    res += 1
                r_cnt = 0
            #검은 부분이 아니면 r_cnt에 +1
            else:
                r_cnt += 1

        # 행을 한 번 순회했을 때 빈칸이 단어 길이만큼 있으면 res에 +1
        if r_cnt == l:
            res += 1

    # 열 검사
    for a in range(n):
        c_cnt = 0
        for b in range(n):
            if puzzle[b][a] == 0:
                if c_cnt == l:
                    res += 1
                c_cnt = 0

            else:
                c_cnt += 1

        if c_cnt == l:
            res += 1

    print(f"#{i+1} {res}")