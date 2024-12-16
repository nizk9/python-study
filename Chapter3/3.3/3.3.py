#通过METHOD sort对列表进行永久排序
car=['audi','bmw','rr','benz']
car.sort()
print(car)
#通过参数（reverse=true)来反转
car.sort(reverse=True)
print(car)
#临时排序，可以使用sorted函数,参数reverse和sort中的一样作用，一样用法
bicycle=['giant','mereda','forever']
print('here is the original list:')
print(bicycle)

print('\nhere is the sorted list:')
print(sorted(bicycle))

print('\nhere is the original list:')
print(bicycle)
#通过len()函数来确定列表的长度
bicycle=['giant','mereda','forever']
print(len(bicycle))