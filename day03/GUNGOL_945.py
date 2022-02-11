# 딕셔너리를 이용하여, 
# "Pokemon"을 입력하면 "Pikachu", 
# "Digimon"을 입력하면 "Agumon", 
# "Yugioh"를 입력하면 "Black Magician", 
# 그 외의 문자열이 입력되면 "I don't know"를 출력하는 프로그램을 작성

#1. 딕셔너리 만들기
animation = {
    "Pokemon": "Pikachu", 
    "Digimon": "Agumon", 
    "Yuhiwang" : "Black Magician", 
}

word = input
# if word in animation.keys(): #딕셔너리는 자동으로 키값을 반환함
if word in animation:
    print(animation[word])
else:
    print("I don't know")

    # print(animation.get(word,"I don't Know"))
