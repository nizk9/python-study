soilders=[]
for soilder_number in range(30):
    new_soilder={'country':'CN','rank':'master','speed':'high'}
    soilders.append(new_soilder)

for soilder in soilders[:3]:
    if soilder['country']=='CN':
        soilder['country']='USA'
        soilder['rank']='rookie'
        soilder['speed']='low'

for soilder in soilders[:5]:
    print(soilder)
print('...')

#去掉if语句也是相同的效果
for soilder in soilders[:3]:
        soilder['country']='USA'
        soilder['rank']='rookie'
        soilder['speed']='low'

for soilder in soilders[:5]:
    print(soilder)
print('...')

