#要调整元组，不可以直接修改元素，但是可以直接重新赋值
dimensions=(200,50)
print("original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions=(400,100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)