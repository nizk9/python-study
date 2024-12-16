#3.4
list=['nizk','wc','chaochao']
message1=f'Sincerely invite you,{list[0].upper()},to come to have a dinner with me'
message2=f'Sincerely invite you,{list[1].upper()},to come to have a dinner with me'
message3=f'Sincerely invite you,{list[2].upper()},to come to have a dinner with me'
print(message1)
print(message2)
print(message3)

#3.5
cantcome=list.pop(2)
print(f"who can't come is {cantcome}.")

list.insert(2,'hsy')
message3=f'Sincerely invite you,{list[2].upper()},to come to have a dinner with me'
print(message1)
print(message2)
print(message3)

#3.6
list.insert(0,'newcomer1')
list.insert(4,'newcomer2')
list.append('newcomer3')
message1=f'Sincerely invite you,{list[0].upper()},to come to have a dinner with me'
message2=f'Sincerely invite you,{list[1].upper()},to come to have a dinner with me'
message3=f'Sincerely invite you,{list[2].upper()},to come to have a dinner with me'
message4=f'Sincerely invite you,{list[3].upper()},to come to have a dinner with me'
message5=f'Sincerely invite you,{list[4].upper()},to come to have a dinner with me'

print(message1)
print(message2)
print(message3)
print(message4)
print(message5)

#3.7
print("Sorry!I finnally can't invite everyone to come,only two guys can come")
guy1=list.pop(-1)
print(f"Sorry,{guy1}.The order only have two seats after all")
guy1=list.pop(-1)
print(f"Sorry,{guy1}.The order only have two seats after all")
guy1=list.pop(-1)
print(f"Sorry,{guy1}.The order only have two seats after all")
guyI=list[0]
print(f"Hi,{guyI}I'm happy to tell you that you are still on the list!")
guyII=list[1]
print(f"Hi,{guyI}I'm happy to tell you that you are still on the list!")
del list[0]
del list[0]
del list[0]
print(list)
print("It's blank!,OOPS!")

