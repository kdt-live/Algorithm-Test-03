T = int(input())
for t in range(1, T+1):
    N , M = map(int, input().split())
    matrix = []
    result = []
    result_sum = []
    for _ in range(N): # 배열을 이중리스트로 만들기
        num_list = list(map(int, input().split()))
        matrix.append(num_list)

    for k in range(N-M+1): # 파리채 길이 때문에 끝까지 돌면 에러가 남
        for K_2 in range(N-M+1): 
            for i in range(M): # 파리채 크기만큼만 더해주기
                for j in range(M): 
                    result.append(matrix[k+i][K_2+j])
            a = sum(result)
            result_sum.append(a)     
            result = []
    print("#{0} {1}".format(t,max(result_sum))) 

# 이 문제는 강사님이 수업시간에 한번 언급해주신 문제였다.
# 하지만 생소해서... 어떻게 풀어햐하는지 감이 안 와서 낭비한 시간이 크다
# 역시나 이 문제는 저번 백준 문제에 3중 for문처럼 범위만 잘 설정하면 그렇게 어려운 문제는 아니라고 생각한다.
# 하지만 그 범위를 설정하는 것이...어렵다ㅠ
    