#range()函数
for value in range(1,5):
    print(value)

#使用list函数生成数组
numbers=list(range(1,5))
print(numbers)

#使用range生成偶数，（起始，终止，每次加值）
even_numbers=list(range(2,11,2))
print(even_numbers)

#生成平方数的一个例子
squares=[]
for value in range(1,11):
    square=value**2
    squares.append(square)
print(squares)

#更简洁的生成平方数
squares=[]
for value in range(1,11):
    squares.append(value**2)
print(squares)

#统计最大值，最小值，总和
digits=[]
for digit in range(0,10):
    digits.append(digit)
print(min(digits),max(digits),sum(digits))

#列表推导式 list comprehensions
squares=[value**2 for value in range(1,11)]
print(squares)