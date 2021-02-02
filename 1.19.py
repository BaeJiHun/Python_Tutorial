class Stack:
    def __init__(self):
        self.items = []

    def push(self, val):
        return self.items.append(val)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            print("Stack is empty")

    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            print("Stack is empty")

    def __len__(self):
        return len(self.items)


S = Stack()
parseq = []
for p in parseq:
    if p == '(':
        print(S.push(p))
    elif p == ')':
        print(S.pop())
    else:
        print("Not allowed Symbol")

if len(S) > 0:
    print(False)
else:
    print(True)


day = 1
first_height = 7
height = 0
while height < 30:
    day += 1
    height = first_height + 2 * (day - 1)
print(day)

def push(item):
    return s.append(item)

def pop():
    if len(s) == 0:
        print("Stack is empty")
        return
    else:
        return s.pop(-1)

s = []
push(1)
push(2)
push(3)
# print(s)
print("pop item is:", pop())
print("pop item is:", pop())
print("pop item is:", pop())
print("pop item is:", pop())


def factorial(val):
    answer = 1
    for i in range(1, val+1):
        answer *= i
    return answer

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)

print(fact(4))


