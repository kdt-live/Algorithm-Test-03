#230203

# #S5431 민석이의 과제 체크하기
# t=int(input())
# for i in range(t):
#     n,k=map(int,input().split())
#     submit=list(map(int,input().split()))
#     student=[]
#     result=""
#     for j in range(n):
#         student.append(j+1)
#     for k in submit:
#         student.remove(k)
#     for l in range(len(student)):
#         result += str(student[l] )
#         result += " "
#     print(f"#{i+1} {result}")

# #2001 파리퇴치
# t=int(input())
# for nums in range(t):
#     n,m=map(int,(input().split()))
#     matrix=[]
#     sum=0
#     max_sum=0
#     for j in range(n):
#         line=list(map(int,input().split()))
#         matrix.append(line)
#     s_x=s_y=0
#     for s_x in range(0,n-m+1):
#         for s_y in range(0,n-m+1):
#             sum=0
#             for i in range(m):
#                 for j in range(m):
#                     sum+=matrix[s_x+i][s_y+j]
#                 max_sum=max(max_sum,sum)
#     print("#%d %d"%(nums+1,max_sum))
    
#1983 조교의 성적 매기기
# t=int(input())
# scores={
#     0 : "A+", 1 : "A0", 2 : "A-", 
#     3 : "B+", 4 : "B0", 5 : "B-", 
#     6 : "C+", 7 : "C0", 8 : "C-", 
#     9 : "D0"
# }
# for i in range(t):
#     n,k=map(int,input().split())
#     result=[]
#     number=n//10 
#     for j in range(n):
#         score=list(map(int,input().split()))
#         result.append(score[0]*0.35+score[1]*0.45+score[2]*0.2)
#     student_score=result[k-1]
#     result.sort()
#     student_index=result.index(student_score)
#     score_index=n-student_index-1
#     score_index=(score_index)//number
#     print(f"#{i+1} {scores[score_index]}")

# #1979 어디에 단어가 들어갈 수 있을까
t=int(input())
for tc in range(1,t+1):
    n,k=map(int,input().split())
    matrix=[]
    for _ in range(n):
        line=list(map(int,input().split()))
        matrix.append(line)
    ans=0
    for i in range(n):
        cnt_r=0
        for j in range(n):
            if matrix[i][j] ==1:
                cnt_r+=1
            else:
                if cnt_r == k:
                    ans+=1
                cnt_r=0
        if cnt_r == k:
            ans+=1
        cnt_c=0
        for j in range(n):
            if matrix[j][i] == 1:
                cnt_c+=1
            else:
                if cnt_c == k:
                    ans+=1
                cnt_c=0  
        if cnt_c == k:
            ans+=1
    print(f"#{tc} {ans}")

# #1225 암호 생성기
# for i in range(10):
#     t=int(input())
#     num=list(map(int,input().split()))
#     sum=1
#     password=""
#     while num[-1]>0:
#         if num[0]>0:
#             num[0] = num[0]-sum
#             num.append(num[0])
#             num.pop(0)
#             if sum ==5:
#                 sum=1
#             else:
#                 sum+=1
#     if num[-1]<=0:
#         num[-1]=0
#     for k in range(8):
#         password+=str(num[k])
#         password+=" "
#     print(f"#{i+1} {password}")

# #1218 괄호 짝짓기
# for i in range(10):
#     t=int(input())
#     str=input()
#     a=0
#     b=0
#     c=0
#     d=0
#     for j in range(t):
#         if str[j] == "(":
#             a+=1
#         elif str[j]==")":
#             a-=1
#         elif str[j]=="[":
#             b+=1
#         elif str[j]=="]":
#             b-=1
#         elif str[j]=="{":
#             c+=1
#         elif str[j]=="}":
#             c-=1
#         elif str[j]=="<":
#             d+=1
#         elif str[j]==">":
#             d-=1
#     if a==0 and b==0 and c==0 and d==0:
#         print(f"#{i+1} 1")
#     else:
#         print(f"#{i+1} 0")        