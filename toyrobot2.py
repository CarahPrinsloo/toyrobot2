position = [0, 0]

def name_robot():
    name = input('What do you want to name your robot? ')
    while name == '':
        name = input('What do you want to name your robot? ')
    print_name(name)
    print_greeting()
    return name

def print_name(name):
    print(name, end = '')
    print(': ', end = '')

def print_greeting():
    print('Hello kiddo!')


def turn_off_robot():
    print('Shutting down..')


def print_list_commands(list_commands, list_explanation):
    i = 0
    print('I can understand these commands:')
    for command in list_commands:
        space = 0
        print(command, end = '')
        while space < 6 - (len(command)-1):
            if space == 4 - (len(command)-1):
                print('-', end = '')
            else:
                print(' ', end = '')
            space += 1
        print(list_explanation[i])
        i += 1
    print()


def list_commands_output(list_commands, list_explanation):
    '''Returns string of the output that will print when user enters help command'''
    
    output = 'I can understand these commands:\n'
    i = 0
    for command in list_commands:
        space = 0
        output = output + str(command)
        while space < 6 - (len(command)-1):
            if space == 4 - (len(command)-1):
                output = output + '-'
            else:
                output = output + ' '
            space += 1
        output = output + list_explanation[i] + '\n'
        i += 1
    output = output + '\n'
    return output


def get_steps(command):
    temp_num = 0
    str_num = ''
    for i in range(len(command)):
        try:
            temp_num = int(command[i])
            str_num = str_num + command[i]
        except:
            continue
    if len(str_num) == 0:
        return 'no_steps'
    return str_num


def get_move(command):
    temp_num = 0
    move = ''
    for i in range(len(command)):
        try:
            temp_num = int(command[i])
            continue
        except:
            move = move + command[i]
    return move.lower().strip()


def move_robot_forward(name, steps):
    global position
    
    position[1] = position[1] + int(steps)
    print(' > ' + str(name) + ' moved forward by ' + str(steps) + ' steps.')
    print(' > ' + str(name) + ' now at position ' + '(' + str(position[0]) + ',' + str(position[1]) + ')' +'.')


def move_robot_backwards(name, steps):
    global position

    position[1] = position[1] - int(steps)
    print(' > ' + str(name) + ' moved back by ' + str(steps) + ' steps.')
    print(' > ' + str(name) + ' now at position ' + '(' + str(position[0]) + ',' + str(position[1]) + ')' +'.')


def move_robot_right(name):
    global position

    print(' > '+ str(name) +' turned right.')
    print(' > ' + str(name) + ' now at position ' + '(' + str(position[0]) + ',' + str(position[1]) + ')' +'.')


def move_robot_left(name):
    global position

    print(' > '+ str(name) +' turned left.')
    print(' > ' + str(name) + ' now at position ' + '(' + str(position[0]) + ',' + str(position[1]) + ')' +'.')


def turn_command_into_tuple(command):
    """format: (move, steps); if no steps are provided then steps = no_steps"""
    tup_command = (get_move(command), get_steps(command))
    return tup_command


def choose_command(command, list_commands):
    """Returns tuple with move and steps; ONLY if it's a valid move"""
    tuple_command = turn_command_into_tuple(command.lower().strip())
    for item in list_commands:
        if item.lower() == tuple_command[0]:
            return tuple_command
    return ('not_option', 'no_steps')


def do_command(tuple_command, list_commands, list_explanations, name):
    if  tuple_command[0] == 'off':
        turn_off_robot()
        return True
    elif tuple_command[0] == 'help':
        print_list_commands(list_commands, list_explanations)
    elif tuple_command[0] == 'forward':
        move_robot_forward(name, tuple_command[1])
    elif tuple_command[0] == 'back':
        move_robot_backwards(name, tuple_command[1])
    elif tuple_command[0] == 'right':
        move_robot_right(name)
    elif tuple_command[0] == 'left':
        move_robot_left(name)
    return False


def robot_start():
    """This is the entry function, do not change"""
    name = name_robot()
    off = False
    list_commands = ['OFF', 'HELP', 'FORWARD', 'BACK', 'RIGHT', 'LEFT']
    list_explanations = ['Shut down robot', 'provide information about commands', 'move robot forward', 'move robot backwards', 'turns robot right', 'turns robot left']

    while not off:
        print_name(name)
        command = input('What must I do next? ')
        while choose_command(command, list_commands)[0] == 'not_option':
            print('Sorry, I did not understand ', end = '')
            print('\'' + command + '\'.')
            command = input('What must I do next? ')
        tuple_command = choose_command(command, list_commands)
        off = do_command(tuple_command, list_commands, list_explanations, name)


if __name__ == "__main__":
    robot_start()
