multiline = """
Life is short
You need python
"""

print(multiline)

say = 'Python\'s good'
print(say)

a = "python"
b = " is fun"
print(a+b)

c = "="
print (c * 50)
d = "my life"

print(c * 50 )
print(d)
print(c * 50)

a = "Life is good"
print(len(a))
print(a[5])
print(a[-2])
print(a[:4])

a = "2020년 12월 28일 cloudy"
year = a[:5]
date = a[6:13]
weather = a[14:]

print(year)
print(date)
print(weather)

a = 'Bae Gi Hun'
first_name = a[5:]
last_name = a[:3]
print(last_name + 'J' + first_name)
print(" i eat %d apples" %3)
print(" i eat %s apples" % "three")

number = 3
print("i eat %d apples" % number)
date = "ten"
print(" i eat %d apples. so i sick for %s days " % (number, date))

print("i got a 100 score about %d%% " % 99)

print("%.6f" %3.25451143)

print("i eat {} apples".format(3))
print("i eat {0} apples and {1} strawberries".format(3,2))
print("i eat {number} apples and i sick for {date} days".format(number = 3, date = 5))
print("i eat {0} apples and i sick for {date} days".format(3, date=5))

y = 3.43124134
print("{0:10.4f}".format(y))

name = '배지훈'
age = '26'
print(f"제 이름은 {name} 이고, 제 나이는 {age} 입니다.")

age = 26
print(f"내년의 내 나이는 {age + 1} 살입니다")

print(f'{"hi":^10}')
print(f'{"hi":!<10}')
print(f'{"It`s me":!<10}')
y= 3.1415926535897932384626433832795028841971693993751058209749445923
print(f'{y:<10.5f}')

a = "hobby"
print(a.index("b"))

a = "Life is good"
print(a.split())


a = [1,2,3]
print(str(a[2]) + "hi")
print(str(3) + "hi")

a = [1,2,3]
a.append(4)
print(a)
a.insert(4,5)
print(a)

t1 = [1,2,3]
t1[0] = "c"
print(t1)

dic = {'name': 'jihun' , 'age' : '26' , 'birth' : '0319'}
print(dic['name'])
print(dic['age'])
print(dic['birth'])

dic['live'] = 'gwangju'
print(dic)

del dic['birth']
print(dic)

print(dic['name'])

a = {(1,2) : 'hi'}
print(a)

print(dic.keys())
for i in dic.keys():
    print(i)

print(list(dic.keys()))

print(dic.values())
print(list(dic.values()))

print(dic.items())
print(list(dic.items()))

print(dic.clear())

s1 = set([1,2,3])
print(s1)

s2 = list(s1)
print(s2)

s1 = set([1,2,3])
s2 = set([2,3,5,6])

print(s1&s2)
print(s1.intersection(s2))

print(s1|s2)
print(s1.union(s2))

print(s2-s1)
print(s1-s2)
print(s1.difference(s2))
print(s2.difference(s1))

pin_number = "8811201068234"
year_month_day = ymd = pin_number[:6]
print(ymd)
back_number = bn = pin_number[6:]
print(bn)

a = "a:b:c:d"
b = a.replace(":", "#")
print(b)

a = [1,3,5,4,2]
a.sort()
a.reverse()
print(a)

a = ['Life' , 'is' , 'too' , 'good']
sentence = " ".join(a)
print(sentence)

a = (1,2,3)
print(id(a))
a += (4,)
print(id(a))

treehits = 0
while treehits < 10:
    treehits += 1
    print("나무를 %d 찍었습니다." %treehits)
    if treehits == 10:
        print("나무 넘어간다")

a = [[1,2] , [3,4], [5,6]]
for [first,last] in a:
    print(first + last)

marks = [90,50,80,45,75]
number = 0
for i in marks:
    number += 1
    if i > 60:
        print("%d 넌 합격" % number)
    else:
        print("%d 넌 불합격" % number)

marks = [90,50,80,45,75]
for number in range(len(marks)):
    if marks[number] >60:
        print("%d 넌 합격" % (number+1))
    else:
        print("%d 넌 불합격" % (number+1))

for i in range(2,10):
    for j in range(1,10):
        print(i*j, end = " ")
    print(' ')

a = [1,2,3,4]
result = []
for i in a:
    result.append(i*3)
print(result)

a = [1,2,3,4]
result = [i*3 for i in a]
print(result)

a = [1,2,3,4]
result = [i*2 for i in a if i % 2 == 0]
print(result)


result = [i*j for i in range(2,10)
          for j in range(1,10)]
print(result)


result = 0
i = 1
while i < 1000:
    i += 1
    if i % 3 == 0:
        result += i
print(result)


i = 0
while i <5:
    i += 1
    print("*" * i)

for i in range(1,101):
    print(i)

A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
avg = 0
for a in A:
    avg += a / 10
print(avg)


numbers = [1, 2, 3, 4, 5]
result = [n*2 for n in numbers if n % 2 == 1 ]
print(result)

def add(a,b):
    return a+b
print(add(3,4))

def add(a,b):
    result = a+b
    return result

def introduce():
    return("저는 배지훈입니다")

print(introduce())

def add(a,b):
    print("%d와 %d의 합은 %d 입니다" % (a,b,a+b))

print(add(3,4))

def say():
    print('Hi')

print(say())

def add(*args):
    result = 0
    for i in args:
        result += i
    return result
print(add(1,2,3))
print(add(1,2,3,4,4,5,6,6,7))

def mul_cal(choice,*args):
    if choice == 'sum':
        result = 0
        for i in args:
            result += i
        return result
    elif choice == 'mul':
        result = 1
        for i in args:
            result *= i
        return result
print(mul_cal('sum', 1,2,3))
print(mul_cal('mul', 1,2,3,4,5))

def add_mul(a,b):
    return a+b, a*b

ans1, ans2 = add_mul(3,4)
print(ans1, ans2)

def say_nick(nick):
    if nick == '바보':
        return
    else:
        print("나의 별명은 %s 입니다" % nick)
print(say_nick('천재'))
print(say_nick('바보'))

def introduce(name, age, 전남대 = True):
    print("나의 이름은 %s 입니다" % name)
    print("나의 나이는 %d 입니다" % age)
    if 전남대:
        print("제 학교는 전남대입니다")
    else:
        print("제 학교는 전남대가 아닙니다")

print(introduce('배지훈',26))
print(introduce('배지훈', 26, False))

def vartest(a):
    a += 1
    return a
print(vartest(3))

fcn = lambda x: x**2 -1
ans = fcn(4)
print(ans)

def is_odd(n):
    if n % 2 == 0:
        print("이 수는 짝수입니다")
    else:
        print("이 수는 홀수입니다.")
print(is_odd(2))
print(is_odd(4))

def avg_fcn(*args):
    avg = 0
    for i in args:
        avg += i / len(args)
    return avg
print(avg_fcn(1,2,3,4,5))

# input1 = int(input("첫번째 숫자를 입력하세요:"))
# input2 = int(input("두번쨰 숫자를 입력하세요:"))
#
# total = input1 + input2
# print("두 수의 합은 %s입니다." % total)

print("you" "need" "python")
print("you"+"need"+"python")
print("you", "need", "python")
print("".join(["you", "need", "python"]))

def add(a,b):
    result = 0
    c = a+b
    result += c
    return result
print(add(1,2))

def add(*args):
    result = 0
    for i in args:
        result += i
    return result

print(add(1,2,3))

result = 0
def add(num):
    global result
    result += num
    return result
print(add(3))
print(add(4))
print(add(2))

class fourcal:
    def setdata(self,first,second):
        self.first = first
        self.second = second
a = fourcal()
a.setdata(4,2)
print(a.first)
print(a.second)

a = fourcal()
b = fourcal()

a.setdata(4,2)
b.setdata(3,7)
print(a.first)
print(b.first)
print(a.second)
print(b.second)

class fourcal:
    def setdata(self,first,second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

a = fourcal()
a.setdata(4,2) #초기값    ㅡ> 생성자 : (__init__) 사용 // 초기값설정해야할 때
print(a.add())
print(a.mul())

class fourcal:
    def __init__(self,first,second):
        self.first = first
        self.second = second

    def setdata(self,first,second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

a = fourcal(4,2)
print(a.add())

class morefourcal(fourcal):
    def pow(self):
        result = self.first ** self.second
        return result

a = morefourcal(4,2)
print(a.pow())

class calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

a = calculator()
a.add(4)
print(a.value)

class UpgradeCalculator(calculator):
    def minus(self,val):
        self.value -= val

cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)
print(cal.value)

class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        if self.value > 100:
            self.value = 100

cal = MaxLimitCalculator()
cal.add(50)
cal.add(60)
print(cal.value)

print(round(17/3, 4))

# def multiple():
#     result = []
#     for i in range(2,10):
#         for j in range(1,10):
#             result.append(i*j)
#     return result
#
# print(multiple())

def multiple(n):
    result = []
    i = 0
    while i <10:
        i += 1
        result.append(n*i)

    return result

print(multiple(2))

result = 0
for i in range(1,1000):
    if i % 3 == 0 or i % 5 == 0:
        result += i
print(result)


def gettotalpage(post,page):
    if post % page == 0:
        return post // page
    else:
        return post // page + 1

print(gettotalpage(24,10))
print(gettotalpage(30,10))

A = [20, 55, 67,82, 45, 33, 90, 87, 100, 25]
result = 0
for i in A:
    if i > 50:
        result += i
print(result)

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-2) + fib(n-1)

for i in range(10):
    print(fib(i))

# user_input = input("숫자를 입력하세요:")
# numbers = user_input.split(",")
# total = 0
# for i in numbers:
#     total += int(i)
# print(total)

class Calculator:
    def __init__(self, list):
        self.list = list

    def sum(self):
        result = 0
        for i in self.list:
            result += i
        return result

    def avg(self):
        average = 0
        for i in self.list:
            average += i / len(self.list)
        return average

cal1 = Calculator([1,2,3,4,5])
print(cal1.sum())
print(cal1.avg())

cal2 = Calculator([6,7,8,9,10])
print(cal2.sum())
print(cal2.avg())


