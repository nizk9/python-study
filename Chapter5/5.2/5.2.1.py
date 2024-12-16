#通过==两个等号来检验条件为真或假
cars=['bmw','benz','toyota','HOnda','byd']
for car in cars:
    if car=='byd':
        print(car.upper())
    else:
        print(car.title())

car='honda'
print(car=='honda')

#通过！=来验证是否不相等
requested_topping='mashroom'
if requested_topping!='anchovies':
    print("Hold the anchovies!")

#数值检验
COUNT=0
Basic_number=range(1,51)
for int in Basic_number:
    if int!=13:
        COUNT=COUNT+1
print(f"There are {COUNT} number except 13")

#and or not，即数学逻辑中的，与，或，非
age_0=22
age_1=18
结果一=age_0>=21 and age_1>=21
print(f"第一个结果是：{结果一}")
age_1=22
结果二=age_0>=21 and age_1>=21
print(f"第二个结果是：{结果二}")
