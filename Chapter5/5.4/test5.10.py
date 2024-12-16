current_users=['marshall','orange','fender','gibson','nizk']
new_users=['MArshall','nizk','edwards','ESP','mesa boogie']
for new_user in new_users:
    if new_user.lower() in current_users:
        print(f"Sorry,your user name {new_user} have been used!")
    else:
        print(f"Congradulation!Your user name {new_user} can be used.")