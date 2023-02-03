for _ in range(1,11):
    sentence_length = int(input())
    sentence = input(); stack = []; flag = 1
    dictionary = {"{" : "}", "[" : "]", "(" : ")", "<" : ">"}
    for i in range(sentence_length):
        if sentence[i] in dictionary.keys():
            stack.append(sentence[i])
        else:
            tmp = stack.pop()
            if dictionary[tmp] == sentence[i]: pass
            else:
                flag = 0
                print("#{} {}".format(_, 0))
                break
    if flag == 1: print("#{} {}".format(_, 1))