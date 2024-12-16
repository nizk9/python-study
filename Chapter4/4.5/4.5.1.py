#元组，不使用[]创建，而是使用()创建,元组中的元素不可被更改
dimensions=(200,50)
print(dimensions[0])
print(dimensions[1])

#即便元组中只含有一个元素，也要加逗号
my_t=(3,)
print(my_t)

#遍历元组中的所有数值，操作和前面的list的操作类似
dimension=(12.0,50.25)
for dimen in dimension:
    print(dimen)

