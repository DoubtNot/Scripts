import maya.cmds as cmds

def calculate(num_list, oper_type):
    operator = ''
    total = 0

    if oper_type in ['add', 'subtract', 'multiply', 'divide']:
        if oper_type == 'add':
            operator == '+'

        if oper_type == 'subtract':
            operator == '-'

        if oper_type == 'multiply':
            operator == '*'

        if oper_type == 'divide':
            operator == '/'

        num_str = (", ".join(map(str, num_list)))
        total = num_list.pop(0)

        for num in num_list:
            total =