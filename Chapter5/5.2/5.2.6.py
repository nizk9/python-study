#检查特定的值是否在列表中
requested_toppings=['mushrooms','onions','pineapple']
print('mushrooms' in requested_toppings)
print('pepperoni' in requested_toppings)

#检查是否不在列表中
banned_users=['david','john','Mr.right']
user='marie'

if user not in banned_users:
    print(f"{user.title()},you are not banned user!")