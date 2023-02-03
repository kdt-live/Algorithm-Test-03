# 조교의 성적 매기기 D2

# 학생들 각각의 총점을 구해서 리스트에 넣고
# N(학생수) / 10 = ?명의 학생들에게 동일한 평점을 부여함

score = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]
T = int(input())  # 테스트 케이스 개수 : 10

for t in range(1, T+1):  # T loop 10 times
    # 학생수 N 과, 학점을 알고싶은 학생의 번호 K
    N, K = map(int, input().split())

    total_list = []  # 학생마다 총점 배열에 저장할 total_list
    for _ in range(N):  # students loop N times
        mid, final, assi = map(int, input().split())
        # 총점 구하는 식
        total = (mid * 0.35) + (final * 0.45) + (assi * 0.2)
        total_list.append(total)
    # total_list = [74.6, 92.55000000000001, 88.8, 99.45, 72.35, 85.85000000000001, 96.25, 68.95, 85.5, 85.75]

    # k번 학생의 인덱스 구해서 k번학생의 총점 구하기
    k_score = total_list[K-1]  # k가 2일때 인덱스는 2-1해줘야 위치를 찾음
    # 92.55000000000001

    # sort만 하면 오름차순인데
    # 문제에서 '10 개의 평점을 총점이 높은 순서대로 부여'한다고 명시
    # 평점을 내림차순으로 정렬
    total_list.sort(reverse=True)
    # print(total_list)

    # N 명의 학생이 있을 경우 N/10 명의 학생들에게 동일한 평점을 부여
    same_total = N // 10  # 1

    # k번째 학생의 총점으로 index 위치 찾고
    # 그 위치와 same_total을 나누기
    k_final = total_list.index(k_score) // same_total
    # 2 // 1 == 2

    # k번째 학생의 학점
    print(f'#{t} {score[k_final]}')


# 코드로 구현하는 것보다 문제를 이해하는데 시간을 너무 많이 소비한 문제..
