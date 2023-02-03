# 조교의 성적 매기기

T = int(input())
for t in range(1, T + 1):
    students, K = list(map(int,input().split()))
    lists = []
    for scores in students:
        mid, fin, assgn = list(map(int,input().split()))
        lists.append((mid * 0.35) + (fin + 0.45) + (assgn * 0.2))
    s_lists = sorted(lists)[::-1]
    rank = s_lists.index(lists[K])
    if rank // (students // 10) :
        print("D0")
        

    
# K = 2
# lists = [80, 38, 58, 19, 90, 37, 83, 80, 91, 58]
# s_lists = sorted(lists)[::-1]
# print(s_lists)
# rank = s_lists.index(lists[K])
# print(rank)
# K_score = 0
# ABC = []
# for s in range(0, len(s_lists), len(lists) // 10):
#     ABC.append(s_lists[s:s+len(lists)//10])
# print(ABC)