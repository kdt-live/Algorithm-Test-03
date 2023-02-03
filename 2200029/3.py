import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(1, T + 1):
    N, k = list(map(int, input().split()))
    total = []
    for n in range(1, N + 1):
        exam1, exam2, exam3 = list(map(int, input().split()))
        score = exam1 * 0.35 + exam2 * 0.45 + exam3 * 0.2
        total.append(score)
        if n == k:
            k_score = score
    # print(total)
    dict = {}
    # print(total)
    total = sorted(total, reverse = True)
    # print(total)
    cnt = N // 10  # 각 점수당 학생 수
    dict["A+"] = total[:cnt * 1]
    dict["A0"] = total[cnt * 1:cnt * 2]
    dict["A-"] = total[cnt * 2:cnt * 3]
    dict["B+"] = total[cnt * 3:cnt * 4]
    dict["B0"] = total[cnt * 4:cnt * 5]
    dict["B-"] = total[cnt * 5:cnt * 6]
    dict["C+"] = total[cnt * 6:cnt * 7]
    dict["C0"] = total[cnt * 7:cnt * 8]
    dict["C-"] = total[cnt * 8:cnt * 9]
    dict["D0"] = total[cnt * 9:cnt * 10]
    for key in dict:
        if k_score in dict[key]:
            print(f'#{t} {key}')
    

    


