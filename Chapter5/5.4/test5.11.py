sequence=list(range(1,10))
print(sequence[:])
for number in sequence:
    if number <= 1:
        print("1st")
    elif 1 < number <= 2:
        print("\n2nd")
    elif 2 < number <=3:
        print("\n3rd")
    else:
        print(f"\n{number}th")
