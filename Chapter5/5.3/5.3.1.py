#if语句
#if conditional_test：
#   do something
#如果condition为真，则执行后续
age=19
if age>=18:
    print("You are old enough to vote!")
    print("\nHave you registered to vote yet?")

#else,可有可无，如果if为真，else无效，如果if为假，else有效
age=17
if age>=19:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry,you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")


