#直接修改列表元素值
vehicle=['honda','toyota','suzuki']
print(vehicle)
vehicle[2]='MG'
print(vehicle)
#在列表末尾添加元素 .append
vehicle=['honda','toyota','suzuki']
print(vehicle)
vehicle.append('volks wagen')
print(vehicle)

vehicle=[]
vehicle.append('volks wagen')
vehicle.append('honda')
vehicle.append('honda')
print(vehicle)

#在列表中插入元素 .insert
vehicle=['honda','toyota','suzuki']
vehicle.insert(2,'volks wagen')
print(vehicle)

#删除元素 del
vehicle=['honda','toyota','suzuki']
del vehicle[0]
print(vehicle)

vehicle=['honda','toyota','suzuki']
del vehicle[2]
print(vehicle)

#弹出元素 .pop()
vehicle=['honda','toyota','suzuki']
print(vehicle)
popped_vehicle=vehicle.pop()
print(vehicle)
print(popped_vehicle)

#弹出任意一个元素 .pop
vehicle=['honda','toyota','suzuki']
print(vehicle)
popped_vehicle=vehicle.pop(0)
print(vehicle)
print(popped_vehicle)

vehicle=['honda','toyota','suzuki']
message=f'My first car is {vehicle.pop(0)}'
print(message)

#不通过排序而通过搜索值删除 remove
vehicle=['honda','toyota','suzuki']
vehicle.remove('honda')
print(vehicle)

