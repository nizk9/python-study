#测试多个条件,此时不要利用elif，否则只会进行至多一个if检验，所以需要用多个if
requested_toppings=['mushrooms','extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")