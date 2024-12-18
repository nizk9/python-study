pets={'coco':{'master':'rocky','species':'corky'},
      'mumu':{'master':'alice','species':'labrador'}}
for pet,pet_info in pets.items():
    name=pet
    master=pet_info['master']
    species=pet_info['species']

    print(f"Cute {name.title()}'s master is {master.title()},species is {species.title()}")