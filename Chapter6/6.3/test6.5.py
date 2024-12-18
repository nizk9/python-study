rivers={'Nile':'Egypt','Yellow river':'China',
        'Yagezte river':'China','mixixibi':'USA'}
for i,j in rivers.items():
    print(f'The {i} runs through {j}.')

for i in rivers.keys():
    print(i)

for j in rivers.values():
    print(j)

#添加了FUJI和JAPAN这一对到原始的字典中
rivers['FUJI']='japan'
print(rivers)