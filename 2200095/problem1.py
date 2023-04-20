# 1218. [S/W 문제해결 기본] 4일차 - 괄호 짝짓기
plus = ['(', '[', '{', '<']
minus = [')', ']', '}', '>']
total = ['(', '[', '{', '<', ')', ']', '}', '>']
for _ in range(10):
    input()
    score = list(map(int, [0, 0, 0, 0]))
    input_list = list(input())
    flag = True
    for i in input_list:
        if flag :    
            for x, index in zip(plus, range(4)):
                if i == x:
                    score[index] += 1
            for y, index in zip(minus, range(4)):
                if i == y:
                    if score[index] >= 0:
                        score[index] -= 1
                    else:
                        print(f'#{_ + 1} 0')
                        flag = False
    if flag:
        if score == [0, 0, 0, 0]:
            print(f'#{_ + 1} 1')
        else:
            print(f'#{_ + 1} 0')
