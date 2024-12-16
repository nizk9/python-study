**Chapter6:字典**
function:

items:
    **字典**：
    1、字典 元素={'键1',值,'键2':值,以此类推,使用","分割键值对,使用"："分割键值},修改参数时，只需重新对项目进行赋值.删除时,和列表一样使用del命令进行删除.
    2、一个'项目':参数构成整体,称为一个键值对
    3、遍历访问字典中的每一个键值对:
    for k,v in example()，格式中k代表键，v代表值，
    *例0*：重新赋值
        alien_0['speed']='fast'
    *例1*:添加键值对
        alien_0={'color':'green','points':5}
        print(alien_0)
        alien_0['x_position']=0
        alien_0['y_position']=25
        print(alien_0)
    *例2*:从空字典开始创建
        alien_0={}
        alien_0['color']='green'
        alien_0['points']=5
        print(alien_0)

methods:
    **.items()**:访问键值对
    **.keys()**:访问键
    **.values()**:访问值