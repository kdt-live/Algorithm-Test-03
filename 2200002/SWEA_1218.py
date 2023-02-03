


for tc in range(10):
    N = int(input())
    list1 = list(map(str, input()))
    list2 = list()

    left = ['(', '{', '[', '<']
    right = [')', '}', ']', '>']

    for i in range(N):
        if list1[i] in left:
            list2.append(list1[i])
        if list1[i] in right:
            if right.index(list1[i]) == left.index(list2[-1]):
                list2.pop()
            else:
                break

    cnt = 0
    if len(list2) == 0:
        cnt = 1

    print("#{} {}".format(tc + 1, cnt))