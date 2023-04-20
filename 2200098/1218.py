import sys
sys.stdin = open('1218.txt', 'r')
T = 10
for t in range(1, T+1):
    brct = {'()': 0, '[]': 0, '{}': 0, '<>': 0}
    l = int(sys.stdin.readline())
    word = sys.stdin.readline()
    answer = 1
    for i in range(l):
        if word[i] == '(' : brct['()'] += 1
        elif word[i] == ')' :
            brct['()'] -= 1
            if brct['()'] < 0 :
                answer = 0; break;
        if word[i] == '[' : brct['[]'] += 1
        elif word[i] == ']' :
            brct['[]'] -= 1
            if brct['[]'] < 0 :
                answer = 0; break;
        if word[i] == '{' : brct['{}'] += 1
        elif word[i] == '}' :
            brct['{}'] -= 1
            if brct['{}'] < 0 :
                answer = 0; break;
        if word[i] == '<' : brct['<>'] += 1
        elif word[i] == '>' :
            brct['<>'] -= 1
            if brct['<>'] < 0 :
                answer = 0; break;
    for value in brct.values():
        if value != 0:
            answer = 0
    print('#' + str(t), answer)