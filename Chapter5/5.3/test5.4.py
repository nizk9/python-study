bouns_alien_color=['red','yellow']
killed_alien='red'
if killed_alien in bouns_alien_color:
    print("You got 10 points!")
else:
    print("You got 5 points!")

killed_alien='red'
if killed_alien not in bouns_alien_color:
    print("You got 5 points!")
else:
    print("You got 10 points!")

