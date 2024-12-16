#3.8
destination=['tokyo','newyork','qingdao','mars','berlin']
print(destination)

print(sorted(destination))
print(destination)

print(sorted(destination,reverse=True))
print(destination)
#METHOD reverse可以反转列表中的元素顺序
destination.reverse()
print(destination)

destination.reverse()
print('地名',destination)

destination.sort()
print(destination)
destination.sort(reverse=True)
print(destination)

#3.9
number=len(destination)
print(f'I have {number} places to go')