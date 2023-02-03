score_li = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
students, num = map(int, input().split())
total_dict = {}
total_li = []
for i in range(1, students+1):
    a, b, c = map(int, input().split())
    # 총점계산
    total = (a*0.35) + (b*0.45) + (c*0.2)
    total_dict[i] = total
    total_li.append(total)

head = students // 10
total_li.sort()
score_dict = {}
for i in score_li:
    for j in range(head):
        pass
