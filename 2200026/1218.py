# 괄호 짝짓기 D4

for i in range(1, 11):
    T = int(input())  # 테스트 케이스의 길이
    bracket = list(input())

    # 왼쪽 브라켓 개수를 센다
    # 오른쪽 브라켓 개수를 세서
    # 왼쪽 오른쪽 개수가 일치하는지 판별 후 출력
    left_square = bracket.count('[')
    right_square = bracket.count(']')

    left_curly = bracket.count('{')
    right_curly = bracket.count('}')

    left_parenthese = bracket.count('(')
    right_parenthese = bracket.count(')')

    left_angle = bracket.count('<')
    right_angle = bracket.count('>')

    if left_square == right_square:
        if left_curly == right_curly:
            if left_parenthese == right_parenthese:
                if left_angle == right_angle:
                    print(f'#{i} 1')
                else:
                    print(f'#{i} 0')
            else:
                print(f'#{i} 0')
        else:
            print(f'#{i} 0')
    else:
        print(f'#{i} 0')

# 생각해보니까 pop, append이용하면 코드가 더 간결해질 것 같은데
# if else문 사용해서 좀 지저분한 것 같다..
