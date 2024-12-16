**Chapter4:for循环**
function:
    **range()**:
    range函数,可以制定范围，range(a,b,c),数学上：[a,b),c为间隔差.
    *例1*:该循环使用range函数，使得value遍历了1,5中的1-4.
        for value in range(1,5):
            print(value)
    *例2*:生成偶数
        even_numbers=list(range(2,11,2))
            print(even_numbers)
    *例3*:生成平方数
        squares=[]
        for value in range(1,11):
            square=value**2
            squares.append(square)
        print(squares)
    **list()**:
    生成数组,如number=list(range(1,5)),则会生成一个范围为[1,5)的数组列表.

items:
    **for循环语句**:
    for+变量+in+组，可以让变量遍历组中每一个元素,记住加冒号,在for之后的变量如果之前没有单独创建，会自动创建一个新变量.
    *例1*：该for循环会遍历magicians列表中的每一个元素，并且输出
        magicians=['alice','david','carolina']
        for magician in magicians:
            print(magician)
    **元组**:
    类似列表，但是元组中的数据不可被更改，除非直接对整个元组重新赋值.
    创建方式和列表类似，example=(3,5)*元组中的数据即使只有一个，也必须加逗号，与列表不同*,调用方式和列表相同,example[0]
    
special:
    **min,max,sum**:
    统计最大值，最小值，总和
    digits=[]
    for digit in range(0,10):
        digits.append(digit)
    print(min(digits),max(digits),sum(digits))
    **列表推导式** list comprehensions
    squares=[value**2 for value in range(1,11)]
    print(squares)
