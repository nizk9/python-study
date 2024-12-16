#复制遍历
my_foods=['fried chicken','pizza','huiguorou']
friend_food=my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are also:")
print(friend_food)

my_foods.append('milktea')
friend_food.append('cake')
print(my_foods)
print(friend_food)

#直接将编组赋值给另外一个编组不可以，因为这个等号不代表赋值或复制而是代表关联
my_foods=friend_food
print(my_foods)
print(friend_food)
my_foods.append('milktea')
friend_food.append('cake')
print(my_foods)
print(friend_food)