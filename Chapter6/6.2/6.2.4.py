#修改字典中的值
alien_0={'color':'green'}
print(f"The alien is {alien_0['color']}.")

alien_0['color']='yellow'
print(f"The alien is now {alien_0['color']}.")

alien_0={'x_position':0,'y_position':25,'speed':'medium'}
alien_0['speed']='fast'
print(f"Original posiiton:{alien_0['x_position']}")
if alien_0['speed']=='slow':
    x_increment=1
elif alien_0['speed']=='medium':
    x_increment=2
else:
    x_increment=3
alien_0['x_position']=alien_0['x_position']+x_increment
print(f"Now the alien's position is:{alien_0['x_position']}.")