#if elif else，递进条件语句,实际上if本来就是递进关系，一个一个检测，直到条件为假
age=17
if age<4:
    print("Your admission cost is $0.")
elif age<18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")