for t in range(1, 11):
    N = input()
    string = input()
    result = ""
    for s in string: # 열린 괄호들일 경우에 result에 저장
        if s == "(":
            result += s
        elif s == "[":
            result += s
        elif s == "{":
            result += s
        elif s == "<":
            result += s

        elif s == ")": # 닫힌 괄호들일 경우엔
            if result.find("(") == -1: # 열린괄호가 없으면
                result = ")" # result에 (를 넣고
                break # 종료
            else:   # 열린괄호가 있으면
                result = result.replace("(","",1) # 괄호 찾아서 없애기(여기서 1을 안써주면 모든 열린괄호가 사라져서 좀 헤맸다)   
        elif s == "]":
            if result.find("[") == -1:
                result = "]"
                break
            else:
                result = result.replace("[","",1)    
        elif s == "}":
            if result.find("{") == -1:
                result = "}"
                break
            else:
                result = result.replace("{","",1)    
        elif s == ">":
            if result.find("<") == -1:
                result = ">"
                break
            else:
                result = result.replace("<","",1)    

    if result == "":
        print(f"#{t} 1")
    else:
        print(f"#{t} 0")

# 이 문제는... 하나 다 설정해서 풀었다. 
# 아마 반복문으로 깔끔하게 풀 수 있는 방법도 있지 않을까? 하는 생각이 들었다
# 하지만 아직 실력이 부족해서 거기까지는 생각을 못했고...
# 강사님이 너무 어렵게 생각하지말고 풀으라고 하셔서 노가다로 풀긴 했다...
# 마지막 문제까지 풀고 느낀 점은 오히려 D2문제들이 더 어렵다고 느껴지는건... 나만의 착각일까ㅠ
