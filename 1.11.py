# #  substraction
# import random
#
# number1 = random.randint(0,9)
# number2 = random.randint(0,9)
# if number1 < number2:
#     number1,number2 = number2,number1
#
# answer = eval(input(str(number1) + "-" + str(number2) + "는 얼마입니까?"))
#
# if answer == number1 - number2:
#     print("정답입니다!")
# else:
#     print("틀렸습니다.", number1 , "과" , number2, " 의 차는", number1 - number2 , "입니다")
#
# ################################################################
#
# score = eval(input("점수를 입력하세요"))
#
# if score >= 60:
#     grade = 'D'
#     if score >= 70:
#         grade = 'C'
#         if score >= 80:
#             grade = 'B'
#             if score >= 90:
#                 grade = 'A'
# else:
#     grade = 'F'
#
# print(grade)
#
# #ComputeBMI
#
# weight = eval(input("몸무게를 입력하세요:"))
# height = eval(input("키를 입력하세요:"))
#
# pound = 0.45359237
# inch = 0.0254
#
# weight_per_pound = weight * pound
# height_per_inch = height * inch
#
# BMI = weight_per_pound / (height_per_inch ** 2)
#
# if BMI <= 18.5:
#     print("저체중입니다")
# elif BMI < 25:
#     print("정상입니다")
# elif BMI < 30:
#     print("과체중입니다")
# else:
#     print("비만입니다")
#
#
# #세금계산하기 (2009, US)
# statue = eval(input("0 - 1인세대주" + "1 - 부부공동신고\n" +
#                     "2 - 부부개별신고" + "3- 세대주\n"+
#                     "납세자 구분:"))
#
# income = eval(input("당신의 소득을 입력하세요:"))
# tax = 0
#
# if statue == 0:
#     if income <= 8350:
#         tax = income * 0.1
#     elif income <= 33950:
#         tax = 8350 * 0.1 + (income - 8350) * 0.15
#     elif income <= 82250 :
#         tax = 8350 * 0.1 + (33950 - 8350) * 0.15 + (income - 33950) * 0.25
#     elif income <= 171550:
#         tax = 8350 * 0.1 + (33950 - 8350) * 0.15 + (82250 - 33950) * 0.25 + (income - 82250) * 0.28
#     elif income <= 372950:
#         tax = 8350 * 0.1 + (33950 - 8350) * 0.15 + (82250 - 33950) * 0.25 + (171550 - 82250) * 0.28 + \
#               (income - 171550) * 0.33
#     else:
#         tax = 8350 * 0.1 + (33950 - 8350) * 0.15 + (82250 - 33950) * 0.25 + (171550 - 82250) * 0.28 + \
#               (372950 - 171550) * 0.33 + (income - 372950) * 0.35
#
# elif statue == 1:
#     if income <= 16700:
#         tax = income * 0.1
#     elif income <= 67900:
#         tax = 16700 * 0.1 + (income - 16700) * 0.15
#     elif income <= 137050 :
#         tax = 16700 * 0.1 + (67900 - 16700) * 0.15 + (income - 67900) * 0.25
#     elif income <= 208850:
#         tax = 16700 * 0.1 + (67900 - 16700) * 0.15 + (137050 - 67900) * 0.25 + (income - 137050) * 0.28
#     elif income <= 372950:
#         tax = 16700 * 0.1 + (67900 - 16700) * 0.15 + (137050 - 67900) * 0.25 + (208850 - 137050) * 0.28 + \
#               (income - 208850) * 0.33
#     else:
#         tax = 16700 * 0.1 + (67900 - 16700) * 0.15 + (137050 - 67900) * 0.25 + (208850 - 137050) * 0.28 + \
#               (372950 - 208850) * 0.33 + (income - 372950) * 0.35
#
# elif statue == 2:
#     if income <= 8350:
#         tax = income * 0.1
#     elif income <= 33950:
#         tax = 8350 * 0.1 + (income - 8350) * 0.15
#     elif income <=68525 :
#         tax = 8350 * 0.1 + (33950 - 8350) * 0.15 + (income - 33950) * 0.25
#     elif income <= 104425:
#         tax = 8350 * 0.1 + (33950 - 8350) * 0.15 + (68525 - 33950) * 0.25 + (income - 68525) * 0.28
#     elif income <= 186475:
#         tax = 8350 * 0.1 + (33950 - 8350) * 0.15 + (68525 - 33950) * 0.25 + (104425 - 68525) * 0.28 + \
#               (income - 104425) * 0.33
#     else:
#         tax = 8350 * 0.1 + (33950 - 8350) * 0.15 + (68525 - 33950) * 0.25 + (104425 - 68525) * 0.28 + \
#               (186475 - 104425) * 0.33 + (income - 186475) * 0.35
# else:
#     if income <= 11950:
#         tax = income * 0.1
#     elif income <= 45500:
#         tax = 11950 * 0.1 + (income - 11950) * 0.15
#     elif income <= 117450 :
#         tax = 11950 * 0.1 + (45500 - 11950) * 0.15 + (income - 45500) * 0.25
#     elif income <= 190200:
#         tax = 11950 * 0.1 + (45500 - 11950) * 0.15 + (117450 - 45500) * 0.25 + (income - 117450) * 0.28
#     elif income <= 372950:
#         tax = 11950 * 0.1 + (45500 - 11950) * 0.15 + (117450 - 45500) * 0.25 + (190200 - 117450) * 0.28 + \
#               (income - 190200) * 0.33
#     else:
#         tax = 11950 * 0.1 + (45500 - 11950) * 0.15 + (117450 - 45500) * 0.25 + (190200 - 117450) * 0.28 + \
#               (372950 - 190200) * 0.33 + (income - 372950) * 0.35
#
# print(round(tax,2))
#
# #로또 당첨
# import random
#
# win_number = random.randint(10,99)
# guess_number = eval(input("당첨번호를 입력하세요:"))
#
# print("복권번호는:",win_number, "입니다.")
# win_number_10digits = win_number // 10
# win_number_1digits = win_number % 10
#
# guess_number_10digits = guess_number // 10
# guess_number_1digits = guess_number % 10
#
# if win_number == guess_number:
#     print("천만원의 상금 받으세요.")
# elif win_number_10digits == guess_number_1digits and win_number_1digits == guess_number_10digits:
#     print("삼백만원 받으세요")
# elif win_number_10digits == guess_number_10digits or win_number_10digits == guess_number_1digits or\
#     win_number_1digits == guess_number_10digits or win_number_1digits == guess_number_1digits:
#     print("백만원 받으세요")
# else:
#     print("꽝")
#
# #이차방정식 근 구하기
# a,b,c = eval(input("a,b,c를 입력하세요:"))
#
# r1 = (-b + (b**2-4*a*c)**0.5) / 2*a
# r2 = (-b - (b**2-4*a*c)**0.5) / 2*a
# r = - b / 2*a
# D = b ** 2 - 4*a*c
#
# if D > 0:
#     print("실근은 {0}이고 {1}입니다.".format(round(r1,6),round(r2,5)))
# elif D == 0:
#     print("실근은 {0} 입니다.".format(int(r)))
# else:
#     print("이 방정식은 실근이 존재하지 않습니다.")
#
a, b, c, d, e, f = eval(input("a,b,c,d,e,f를 입력하세요:"))
# a, b, c, d, e, f = 1.0, 2.0, 2.0, 4.0, 4.0, 5.0

D = a * d - b * c

if D == 0:
    print("이 방정식은 해가 없습니다.")
else:
    x = (e * d - b * f) / D
    y = (a * f - e * c) / D
    print("x는 {0}이고 y는 {1}입니다.".format(int(x), int(y)))


# if D == 0:
#     print("이 방정식은 해가 없습니다.")
# else:
#     print("x는 {0}이고 y는 {1}입니다.".format(int(x), int(y)))
