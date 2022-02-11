# 태보태보 총난타
# 오른쪽, 왼쪽의 각 @수를 출력
# word = "@===@==@=@==(^0^)==@=@===@"
# 공백의 기준 (^0^)
l,r = input().split('(^0^)')

left= l.count('@')
right =r.count('@')

print(left, right)


    