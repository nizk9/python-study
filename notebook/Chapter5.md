**Chapter5:if条件循环、条件检验**
items:
    **相等检验**:
    '=='代表相等
    '!='代表不相等，若成立则结果为True,反之结果为False.
    **不等式检验**:
    '<'小于
    '>'大于
    '<='小于等于
    '>='大于等于
    **逻辑连接**:
    not or and,和数学中非 或 与,相同，逻辑判定方式相同.
    **检验是否存在于列表中**:
    使用in检查
    *例*:检验元素'bmw'是否在cars列表中
        'bmw' in cars
    **if条件循环**:
    1、基本格式为:
        if conditional_test:
            do something
    当检验条件为真的时候执行对应操作.
    2、else
        if conditional_test:
            do plan1
        else:
            do plan2
    检验为真执行1，为假执行2
    3、elif,重复执行直到条件为假
        if condition1:
            do plan1
        elif condition2:
            do plan2
        elif condition3:
            do plan3
        .
        .
        .
        else:
            do planX
    *P.S*:若要实现多个检验，不要使用elif,使用多个if语句即可.
