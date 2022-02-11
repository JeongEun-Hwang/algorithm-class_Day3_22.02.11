# 나는 요리사다
# 우승자와 그의 점수를 구하는 프로그램을 작성
# 총 다섯 개 줄에 각 참가자가 얻은 네 개의 평가 점수가 공백으로 구분되어 주어진다. 첫 번째 참가자부터 다섯 번째 참가자까지 순서대로 주어진다. 
# 항상 우승자가 유일한 경우만 입력으로 주어진다.

# 참가자는 5명
# 전체 점수 입력
# 각 참가자의 전체 점수 합 구하기(sum)
# 참가자 점수중 가장 큰 수(max)
# 출력

max_score =0
max_person =0

# 인원수
for i in range(1,6):
    # 점수
    score = sum(list(map(int,input().split())))
    # 점수 조건
    if score>= max_score:
        max_score = score
        max_person = i

print(max_person,max_score)
 