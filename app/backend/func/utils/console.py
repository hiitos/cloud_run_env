# printの色付け
def print_color(color_name, message):
    
    if message == '-':
        content = '--------------------------------------------------'
    elif message == ' ':
        content = '                                                  '
    elif message == '*':
        content = '**************************************************'
    elif message == '_':
        content = '__________________________________________________'
    elif message == '#':
        content = '##################################################'
    elif message == '^':
        content = '^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^'
    else:
        content = message

    if color_name == 'red':
        color_number = 31
    elif color_name == 'green':
        color_number = 32
    elif color_name == 'yellow':
        color_number = 33
    elif color_name == 'blue':
        color_number = 34
    elif color_name == 'purple':
        color_number = 35
    elif color_name == 'cyan':
        color_number = 36
    else:
        color_number = 37

    result = f"\033[1;{color_number}m{content}\033[0m"
    print(result)
    # return result