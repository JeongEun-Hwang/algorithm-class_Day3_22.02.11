# 직사각형 네개의 합집합의 면적 구하기
# https://blog.naver.com/haeun050/222237132117
# 흰색 도화지가 있다.
# 가로, 세로의 크기가 각각 100

# 좌표의 넓이(10*10)
from pydoc import pager


paper = [[0]*100 for _ in range(100)]

# 도형의 꼭짓점 4개 를 문자열로 입력받는다.
for _ in range(4):
    x1,y1,x2,y2 = map(int,input().split())
    
    for i in range(x1,x2):
         for j in range(y1,y2):
            paper[i][j] =1  # 색칠되면 
# 영역의 넓이 출력(도화지에서 1인 부분을 그냥 다 더한다.)
total =0
for i in range(100):
    for j in range(100):
        total += paper[i][j]
print(total)
    