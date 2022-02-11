num = int(input())
# 빈 딕셔너리 선언
countries = []

for _ in range(num):
    # 나라, 도시 입력하기
    country,city = input().split()      #맞음
    countries[country] = city        #맞음
    
input_country = input()
countries.get(input_country, 'Unkown country')
