# 민석이의 과제 체크하기 D3
T = int(input())  # 테스트 케이스 수

for i in range(1, T+1):
    # N: 수강생 수, K: 과제를 제출한 사람 수
    N, K = map(int, input().split())
    # 과제를 제출한 사람의 번호 리스트 : submit
    submit = list(map(int, input().split()))
    # 수강생의 번호 나열 리스트 만들기 : N_list
    N_list = [i for i in range(1, N+1)]

    # 과제 제출하지 않은 사람의 번호를 집합을 이용해 구하고 리스트로 변환(set은 sort함수 못쓰니까)
    not_submit = list(set(N_list) - set(submit))
    not_submit_sort = sorted(not_submit)  # 오름차순으로 정렬해주기
    # f-string과 asterisk으로 unpacking
    print(f'#{i}', *not_submit_sort)

# 궁금한 점 ========
# 첫번째 시도에서 fail 해서
# submit과 N_list를 integer형태로 받는걸로 바꿨는데
# string으로 받아서 하는거는 왜 안되는지 모르겠다
# vscode에서는 출력이 잘되는데!
