#整数integer 
int=5**2
print(int)
#浮点数float,有些小数位数可能会有错误
fl=0.2+0.1
print(fl)
#除法的输出结果始终是浮点数，即使可以整除
ex1=4/2
print(f'输出的结果：{ex1}')
#运算结果始终是浮点数，只要计算时有浮点数参与
ex2=1+2.0
ex3=2*2.5
ex4=3.0**5
print(ex1,ex2,ex3)
#打数字的时候可以用下划线分组，代替逗号，方便自己阅读
ex5=14_000_000
ex6=14,000,000
print(ex5,ex6)
#同时赋值3个数字
x,y,z=5,4,3
print(x,y,z)
#常量constant，值始终不变
ACCELERATION=9.8
print(ACCELERATION)