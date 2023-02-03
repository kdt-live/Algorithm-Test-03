import sys
sys.stdin = open('input.txt', 'r')

for t in range(1, 11):
    num = int(input())
    tx = input()
    # print(type(tx))
    cnt = 0
    # 리스트 넣기
    ans =[ ]
    # 문자열을 리스트에 하나씩 만들기
    res = list(tx)
    # print(ans)
    cnt = 0
    opens = ['(', '[', '{', '<']
    closes = [')', ']', '}', '>']
    # 열었을때
    # 리스트에 추가하면서 닫는 게 나와서 전 문자와 합이 맞는다면 remove
    # 최종적으로 비어있으면 1 중간에 안되거나 남아있다면 0
    for i in res:
        if i in opens:
            ans.append(i)
        elif i in closes:
            ans.append(i)
            if ans[-1] == ans[-2]:
                ans.remove(ans[-1])
                ans.remove(ans[-1])
            else:
                print(0)
                break
    else:
        print(1)