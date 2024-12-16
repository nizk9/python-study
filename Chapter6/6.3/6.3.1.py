#items():访问键值对，keys():访问键 values:访问值
#遍历访问字典中每一个元素
#for k, v in user_0.items()，通过此格式来遍历访问字典中每一个元素
user_0={
    'username':'efermi',
    'first':'enrico',
    'last':'fermi',
}
for 键,值 in user_0.items():
    print(f"\n键:{键}")
    print(f"值:{值}")

favorite_languages={
    'jen':'python',
    'bensen':'C',
    'Violet':'Java'
}
for name,language in favorite_languages.items():
    print(f"{name.title()}'s favortie programming language is {language.title()}.")