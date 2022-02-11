# 평균은 넘겠지
# 각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 
#  반올림하여 소수점 셋째 자리까지 출력한다

test_case = int(input())

for i in range(test_case):
    score_num= list(map(int,input().split()))   # 내가 짠 부분
    
    avg = sum(score_num)/score_num[0]    # score_num[0] 하는 이유?   
    
    count =0    
   
    for j in score_num:
        if j> avg:
            count +=1

    print("%0.3f%%"%((count / score_num[0]*100)))
#


