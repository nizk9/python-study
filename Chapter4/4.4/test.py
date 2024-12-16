#4.10
my_foods=['fried chicken','pizza','huiguorou','hamburger']
print("The first three items in the list are:")
print(my_foods[:3])

three_foods=[]
for food in my_foods:
    three_foods.append(food)
print("\nThe middle of the three foods is:")
print(three_foods[1:2])
print("\nThe last three foods of the list are:")
print(three_foods[-3:])


