favorite_languages={
    'jen':'Python',
    'bensen':'C',
    'Violet':'Java',
    'edward':'Python',
    'marshall':'Go'
}
for name in favorite_languages.keys():
    print(name.title())

#遍历字典的时候，会默认遍历所有的键，所以第8行的代码，可以替换为12行，效果相同
for name in favorite_languages:
    print(name.title())

favorite_languages={
    'jen':'Python',
    'bensen':'C',
    'Violet':'Java',
    'edward':'Python',
    'marshall':'Go'
}
friends=['bensen','sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")

    if name in friends:
        language=favorite_languages[name].title()
        print(f"\t{name.title()},I see you love {language}!")