
# input 5번 반복해서 받는다 => 세로로 입력
score = [list(map(int, input().split())) for _ in range(5)]
success = 0

for i in range(5):
    total = 0
    for j in range(4):
        total += score[i][j]
    average = total / 4
    if average >= 80:
        success += 1
        print("pass")
    else:
        print("fail")

print(f"Successful : {success}")
