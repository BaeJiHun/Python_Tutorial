# 랜덤 카드뽑기
deck = [x for x in range(52)]
shape = ["스페이드", "클로버", "하트", "다이아몬드"]
value = ["A", "2", "3", '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']


import random
random.shuffle(deck)

for i in range(4):
    shapes = shape[deck[i] // 13]
    values = value[deck[i] % 13]
    print("카드번호", deck[i], "은/는" , shapes, values, "입니다.")

