brackets = {
    ')' : '(',
    ']' : '[',
    '}' : '{',
    '>' : '<'
}

for test_case in range(1, 11):
    string_n = int(input())
    strings = input()
    result = 0

    bracket = []

    for char in strings:
        if char not in brackets.keys():
            bracket.append(char)
        else:
            if bracket[-1] == brackets[char]:
                bracket.pop()
            else:
                result = 0
                break
        
        result = 0 if len(bracket) > 0 else 1
    
    print(f'#{test_case} {result}')