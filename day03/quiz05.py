# subject_num = int(input())

# for i in range(subject_num):
#     score = list(map(int,input().split()))
#     avg = sum(score)/score[0]
#     count =0

#     for j in avg:
#             if j >= 80:
#                 print('pass')
#                 count +=1
#             else:
#                 print('fail')
            
#             print('sucessful :',count)

# score = list(map(int,input().split()))
score = [list(map(int,input().split())) for _ in range(5)]

sucess = 0
for scores in score:
    avg = sum(scores)/4

    if avg >= 80:
            print('pass')
            sucess +=1
    else:
            print('fail')
            
print('sucessful :',sucess)
