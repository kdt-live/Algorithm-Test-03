#1218
t = 0
while t < 10:
    t += 1
    num = int(input())
    pair = str(input())
    # 서로 짝이 갯수가 안맞나 봄
    # ] [ 경우는 찾을 수 없지 않은까 (과제)
    if pair.count("(") == pair.count(")"):
        if pair.count("[") == pair.count("]"):
            if pair.count("{") == pair.count("}"):
                if pair.count("<") == pair.count(">"):
                    print(f"#{t} 1")
                else:
                    print(f"#{t} 0")
            else:
                print(f"#{t} 0")
        else:
            print(f"#{t} 0")
    else:
        print(f"#{t} 0")
