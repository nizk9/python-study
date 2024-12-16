#list,一个list可以包含很多东西比如数字文字
bicycles=['trek','cannondale','redline','specialized','giant']
print(bicycles)
#访问list中的元素，因list并非是想要拿给别人看的，而是后台中的
#通过[number]来访问列表中的元素，例：
print(bicycles[0])
#注意，数数从0开始数
print(bicycles[1])
print(bicycles[3])
#特别的，-1代表最后一个，-2代表倒数第二，也就是说负号则是倒序的号数
print(bicycles[-1])

message=f"My first bicycle was a {bicycles[-1].title()}."
print(message)

