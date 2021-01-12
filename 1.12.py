value = int(input("정수를 입력하시오:"))
if value % 5 == 0 and value % 6 == 0:
    print("{0}은/는 5와 6으로 나누어집니다.:".format(value))
if value % 5 == 0 or value % 6 == 0:
    print("{0}은/는 5 혹은 6으로 나누어집니다.".format(value))
if (value % 5 == 0 or value % 6 == 0) and not(value % 5 == 0 and value % 6 == 0):
    print("{0}은/는 5 혹은 6으로 나누어지지만, 둘 모두로는 나누어지지 않습니다.".format(value))

# 동전
import random

answer = random.randint(0,1)
# print(answer)
guess = eval(input("앞면이 나온다 0, 뒷면이 나온다 1:"))
coin = {0:"앞면" , 1: "뒷면"}

if answer == guess:
    print("추측이 맞았습니다. {0}이 나왔습니다.".format(coin[answer]))
else:
    print("틀렸습니다. {0}이 나왔습니다.".format(coin[answer]))

# 세 자리 복권(X)
import random

lucky_num = random.randint(100,999)
print(lucky_num)
guess = eval(input("세 자리 추첨번호를 입력해주세요:"))

lucky_num1 = lucky_num // 100
lucky_num2 = lucky_num / 10 - 10 * lucky_num1
lucky_num3 = lucky_num - 100 * lucky_num1 - 10 * lucky_num2
guess_num1 = guess // 100
guess_num2 = guess / 10 - 10 * guess_num1
guess_num3 = guess - 100 * guess_num1 - 10 * guess_num2

if lucky_num == guess:
    print("축하합니다. 10000000원의 상금을 받으세요.")
elif (lucky_num1 == guess_num1 and lucky_num2 == guess_num3 and lucky_num3 == guess_num2) or\
        (lucky_num1 == guess_num2 and lucky_num2 == guess_num1 and lucky_num3 == guess_num3) or\
        (lucky_num1 == guess_num2 and lucky_num2 == guess_num3 and lucky_num3 == guess_num1) or\
        (lucky_num1 == guess_num3 and lucky_num2 == guess_num1 and lucky_num3 == guess_num2) or\
        (lucky_num1 == guess_num3 and lucky_num2 == guess_num2 and lucky_num3 == guess_num1):
    print("축하합니다. 3000000원의 상금을 받으세요.")
elif (lucky_num1 == guess_num1 or lucky_num1 == guess_num2 or lucky_num1 == guess_num3) or\
        (lucky_num2 == guess_num1 or lucky_num2 == guess_num2 or lucky_num2 == guess_num3) or\
        (lucky_num3 == guess_num1 or lucky_num3 == guess_num2 or lucky_num3 == guess_num3):
    print("축하합니다. 1000000원의 상금을 받으세요.")
else:
    print("꽝")

# 가위바위보 게임
import random

game = {0: "가위" , 1: "바위" , 2: "보"}

program = random.randint(0,2)
print(program)
user = eval(input("가위:0, 바위:1, 보:2 \n "
                  "무엇을 내시겠습니까?:"))

if user > program:
    if program == 0:
        print("컴퓨터는 {0}입니다. 당신은 {1}입니다. 당신이 졌습니다.".format(game[program], game[user]))
    else:
        print("컴퓨터는 {0} 입니다. 당신은 {1}입니다. 당신이 이겼습니다.".format(game[program], game[user]))
elif user == program:
    print("컴퓨터는 {0} 입니다. 당신도 {1}입니다. 비겼습니다.".format(game[program], game[user]))
else:
    if user != 2:
        print("컴퓨터는 {0} 입니다. 당신은 {1}입니다. 당신이 졌습니다.".format(game[program], game[user]))
    elif program == 0:
        print("컴퓨터는 {0}입니다. 당신은 {1}입니다. 당신이 이겼습니다.".format(game[program], game[user]))

# 삼각형 둘레 계산하기

a,b,c = eval(input("세 변을 입력하세요:"))
round = a+b+c

# 1)
if a+b<=c or b+c<=a or c+a<=b:
    print("입력이 잘못되었습니다.")
else:
    print("둘레는", round, "입니다.")
# 2)
if a+b>c and b+c>a and c+a>b:
    print("둘레는",round,"입니다.")
else:
    print("입력이 잘못되었습니다.")

# repeatsubtraction
import random

number1 = random.randint(0,9)
number2 = random.randint(0,9)
answer = number1 - number2

if number1 < number2:
    number1, number2 = number2, number1

get_answer = eval(input(str(number1) + "-" + str(number2) + "는 얼마입니까?:"))

while number1 - number2 != answer:
    answer = eval(input("답이 아닙니다. 다시입력하세요\n" +
                        str(number1) + "-" + str(number2) + "는 얼마입니까?:"))
    if number1 - number2 == answer:
        print("정답입니다!")

# magic number
import random

magic_number = random.randint(0,100)
print(magic_number)
guess = int(input("0과 100 사이의 마법수를 맞춰보세요.\n" +
                  "마법수는 무엇일까요?:"))
while magic_number != guess:
    if magic_number < guess:
        guess = eval(input("값이 큽니다.\n"
                       "마법수는 무엇일까요?:"))
    else:
        guess = eval(input("값이 작습니다.\n"
                       "마법수는 무엇일까요?:"))

if magic_number == guess:
    print("정답. 마법수는 {0} 입니다.".format(magic_number))

#문제 5개, 맞춘개수, 소요시간
import random
import time

count = 0
correct_answer = 0
number_of_question = 5
starttime = time.time()

while count != number_of_question:
    number1 = random.randint(0,9)
    number2 = random.randint(0,9)

    if number1 - number2 < 0:
        number1, number2 = number2, number1

    answer = eval(input(str(number1) + "-" + str(number2) +\
                        "의 값을 구하시오:"))

    if number1 - number2 == answer:
        print("정답입니다!")

        correct_answer += 1

    else:
        answer = print("정답이 아닙니다.\n" , number1 , "와" , number2 , "의 차는" , number1 - number2 , "입니다.")

    count +=1

endTime = time.time()
Total_time = int(endTime - starttime)
print("정답의 개수는 {0} 개중 {1}개 입니다. 수행시간은 {2}초 입니다.".format(number_of_question, correct_answer, Total_time))



