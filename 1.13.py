# 함수

def gcd(n1,n2):
    GCD = 1
    k = 2

    while n1 >= k and n2 >= k:
        if n1 % k == 0 and n2 % k ==0:
            GCD = k
        k += 1

    return GCD

print(gcd(6,28))

# 소수
def isPrime(number):
    divisor = 2
    while number >= 2:
        if number % divisor != 0:
            divisor += 1
        else:
            break

    return number

def getPentagonalNumber(n):
    if n > 0:
        return n * (3 * n - 1) / 2

def PrintgetPentagonalNumber(num = 100):
    per_number = 10
    count = 0
    n = 1
    while count < num:
        if getPentagonalNumber(n):
            count += 1
            print(n, end = " ")
            if count % per_number == 0:
                print()
            n += 1

print(PrintgetPentagonalNumber())

def sumDigits(n):
    digit = 0
    while n:
        digit += n % 10
        n //= 10                        # 좌항을 우항으로 나눈 값을 좌항에 대입
    return digit

answer = eval(input("하나의 정수를 입력하세요:"))
print(sumDigits(answer))

