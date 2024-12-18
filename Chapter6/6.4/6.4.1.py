#嵌套
soilder_0={'Country':'CN','Rank':'1'}
soilder_1={'Country':'USA','Rank':'2'}
soilder_2={'Country':'RUS','Rank':'3'}
soilders=[soilder_0,soilder_1,soilder_2]

for soilder in soilders:
    print(soilder)

#一次性创建多个组
for soilder_number in range(30):
    new_soilder={'country':'USA','rank':'5','speed':'high'}
    soilders.append(new_soilder)

print(soilders)

print("...")
print(f'Total number of soilders:{len(soilders)}')