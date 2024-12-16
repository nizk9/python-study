#for循环语句，for+变量+in+组，可以让变量遍历组中每一个元素,记住加冒号
magicians=['alice','david','carolina']
for magician in magicians:
    print(magician)

magicians=['alice','david','carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick,{magician.title()}.\n")
print("Thank you,everyone.That was really a great show!")
