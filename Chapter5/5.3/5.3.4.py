#使用多个elif代码块
age=17
if age<4:
    price=0
elif age<18:
    price=25
elif age<65:
    price=40
else:
    price=20
print(f"Your age is {age}\nYour admission cost is ${price}.")

#省略else
age=70
if age<4:
    price=0
elif age<18:
    price=25
elif age<65:
    price=40
elif age>=65:
    price=20
print(f"Your age is {age}\nYour admission cost is ${price}.")