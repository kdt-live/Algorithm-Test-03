A = ''
while True :
    test_num = int(input())
    num_list = list(map(int,input().split()))
    N = 1
    while N != 0:
        for _ in range(5):
            if num_list[7] == 0 :   
                for i in num_list:
                    A += str(i)
                    A += " "
                print(f'#{test_num} {A}')
                A = ''
                N = 0
                break
            if num_list[7] < 0 :
                num_list[7] = 0
                for i in num_list:
                    A += str(i)
                    A += " "
                print(f'#{test_num} {A}')
                A = ''
                N = 0
                break
            b = num_list[0] - (_+1)
            num_list.append(b)
            num_list.remove(num_list[0])