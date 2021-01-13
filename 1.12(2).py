# 최대공약수(gcd) n1, n2
# n1 = eval(input("정수를 입력하세요:"))
# n2 = eval(input("정수를 입력하세요:"))
#
# gcd = 1 #최대공약수 최소값 (서로 소수관계일때)
# k = 2 # 가능한 gcd의 최소값
# while n1 >= k and n2 >= k:
#     if n1 % k == 0 and n2 % k == 0:
#         gcd = k
#     k += 1
# print('{0}과 {1}의 최대공약수는 {2} 입니다.'.format(n1, n2, gcd))

# insert = eval(input("정수를 입력하세요. 입력값이 0이면 종료됩니다.:"))
count_plus = 0
count_minus = 0
list = []

while True:
    insert = eval(input("정수를 입력하세요. 입력값이 0이면 종료됩니다.:"))

    if insert != 0:
        if insert > 0:
            count_plus += 1
        else:
            count_minus += 1

        list.append(insert)
        plus = sum(list)
        average = plus / len(list)

    else:
        break

print("양수의 개수는", count_plus, "개 입니다.")
print("음수의 개수는", count_minus, "개 입니다.")
print("총 합은", plus, "입니다.")
print("평균은", average, "입니다.")

# if insert == 0:
#     print("아무 숫자도 입력하지 않았습니다.")



