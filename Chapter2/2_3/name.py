#f函数的作用是，格式化字符串，按照特定格式输出字符串
first_name="ad"
last_name=" carry"
full_name=f"{first_name}{last_name}"
print(full_name)

#也可以使用加法来实现相同的目的
first_name="ad"
last_name=" carry"
full_name=first_name+last_name
print(full_name)

#手动输出字符与替换字符组装
first_name="ad"
last_name=" carry"
full_name=f"{first_name}{last_name}"
QED=f"You are my {full_name.title()}!"
print(QED)

