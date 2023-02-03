# 8개의 수를 입력받고
# 첫 번째 수를 1(i)T감소한뒤 맨뒤로 감소는 반복회수
# 숫가자 감소할 떄 0보다 작아지는 경우 0으로 유지 프로그램은 종료

import sys
sys.stdin = open('input.txt', 'r')

for t in range(1, 11):
    T = int(input())
    num = list(map(int, input().split()))
    # 앞에 빼고 뒤에 t만큼 빼준다
    i = 1
    while True:
        if i > 5:
            i = 1
        re_num = num.pop(0)
        ap_num = re_num - i
        if ap_num <= 0:
            ap_num = 0
            num.append(ap_num)
            break
        else:
            num.append(ap_num)
        i += 1
    nums = list(map(str, num))    
    num= ' '.join(nums)
    print(f'#{T} {num}')