for i in range(1,11) :
    t = int(input())
    a = list(input())
    cnt = []
    for j in a :
        if j == "(" :
            if ")" not in cnt :
                cnt.append(j)
            else :
                cnt.remove(")")
        if j == ")" :
            if "(" not in cnt :
                cnt.append(j)
            else :
                cnt.remove("(")   

        if j == "[" :
            if "]" not in cnt :
                cnt.append(j)
            else :
                cnt.remove("]")    
        if j == "]" :
            if "[" not in cnt :
                cnt.append(j)
            else :
                cnt.remove("[")   

        if j == "{" :
            if "}" not in cnt :
                cnt.append(j)
            else :
                cnt.remove("}")  
        if j == "}" :
            if "{" not in cnt :
                cnt.append(j)
            else :
                cnt.remove("{")   

        if j == "<" :
            if ">" not in cnt :
                cnt.append(j)
            else :
                cnt.remove(">")  
        if j == ">" :
            if "<" not in cnt :
                cnt.append(j)
            else :
                cnt.remove("<")                                 
    if len(cnt) == 0 :
        print(f'#{i} 1')
    else :
        print(f'#{i} 0')