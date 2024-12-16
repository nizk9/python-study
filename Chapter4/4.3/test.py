#4.3
number20=[]
for number in range(1,21):
    number20.append(number)
print(number20)

#4.4 百万数
#numberM=[]
#for numberm in range(1,1000001):
#    numberM.append(numberm)
#print(numberM)

#百万数求和
numberM=[]
for numberm in range(1,1000001):
    numberM.append(numberm)

print(min(numberM),max(numberM),sum(numberM))

#odd number
odd_number=[]
for odd in range(1,20,2):
    odd_number.append(odd)
print(odd_number)

#3 plus
three=[t*3 for t in range(1,11)]
print(three)

#立方，以及立方推导式
thriple=[]
for th in range(1,11):
    thriple.append(th**3)
print(thriple)

thriple=[]
thriple=[th**3 for th in range(1,11)]
print(thriple)