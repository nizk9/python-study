#在字典中存储列表
pizza={
    'crust':'thick',
    'toppings':['mushrooms','extra cheese'],
}

print(f'You ordered a {pizza['crust']}-crust pizza'
      'with the following toppings:')
for topping in pizza['toppings']:
    print(f'\t{topping}')


users = {
'aeinstein': {'first': 'albert',
              'last': 'einstein',
              'location': 'princeton',
              },
'mcurie': {'first': 'marie',
           'last': 'curie',
           'location': 'paris',
           },
        }

for username,user_info  in users.items():
    print(f'\nUsername:{username}')
    full_name=f'{user_info['first']}{user_info['last']}'
    location=user_info['location']

    print(f'\tFull name:{full_name.title()}')
    print(f'\tLocation:{location.title()}')