# 괄호 짝짓기

bracket_dict = {')': '(', ']': '[', '}': '{', '>': '<'}

for i in range(10):
    length = int(input())
    bracket = input()
    bracket_list = list()
    print(f'#{i + 1}', end = ' ')

    for element in bracket:
        if element in ('(', '[', '{', '<'):
            bracket_list.append(element)
        else:
            if bracket_dict[element] != bracket_list.pop():
                print(0)
                break
    else:
        print(1)