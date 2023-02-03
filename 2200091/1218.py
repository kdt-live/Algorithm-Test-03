import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

for i in range(10):
    l = int(input())
    s = input().strip()
    stack = []
    start = ["{", "[", "(", "<"]
    end = ["}", "]", ")", ">"]

    for char in s:
        # 열린 괄호라면 스택에 삽입
        if char in start:
            stack.append(char)
        else:
            # 닫힌 괄호일 때, 스택이 비어있지 않으면 짝을 찾아줌
            if len(stack) != 0:
                tmp = stack.pop()
                if tmp == start[0] and char == end[0]:
                    continue
                elif tmp == start[1] and char == end[1]:
                    continue
                elif tmp == start[2] and char == end[2]:
                    continue
                elif tmp == start[3] and char == end[3]:
                    continue
                else: # 짝이 맞지 않으면 반복문을 종료하고 결과를 출력
                    print(f"#{i+1} 0")
                    break
            else: # 모든 괄호를 순회하지 않았는데 스택이 비었다면 반복문 종료, 결과 출력
                print(f"#{i+1} 0")
                break
    else: # 모든 괄호를 순회했는데 스택이 비어있지 않다면 짝이 맞지 않았으므로 0 출력
        if len(stack) != 0:
            print(f"#{i+1} 0")
        else:
            print(f"#{i+1} 1")
