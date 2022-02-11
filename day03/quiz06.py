# 흰색 도화지가 있다.
# 가로, 세로의 크기가 각각 100
# 0으로 채워진 이차원 리스트를 100번 반복한다.
from pydoc import pager


paper = [[0]*100 for _ in range(100)]

# 색종이 갯수 받기
n = int(input())
# 색종이 전체 칠하는 로직=========
for _ in range(n):
    # x,y좌표
    x,y = map(int,input().split())
    # 색종이 색을 채울 부분
    for i in range(x,x+10):
         for j in range(y,y+10):
            paper[i][j] ==1  # 색칠되면 
# =======================
# 영역의 넓이 출력(도화지에서 1인 부분을 그냥 다 더한다.)
total =0
for i in range(100):
    for j in range(100):
        total +=paper[i][j]
print(total)