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

num1,num2,num3 = eval(input("세 수를 입력하세요:"))
print(num1,num2,num3)
answer = [2,3,9]
guess = []
# guess += num1, num2, num3
# print(guess)
for num in range(1,11):
    num1, num2, num3 = eval(input("1부터 10사이의 세 수를 입력하세요:"))
    guess += num1, num2, num3
    if guess == answer:
        print("축하합니다. 백만원을 가져가세요.")
    elif

    elif num1 or num2 or num3 in answer:
        print("축하합니다. 십만원을 가져가세요")

