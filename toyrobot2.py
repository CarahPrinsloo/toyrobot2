def name_robot():
    """Name robot"""
    
    name = input('What do you want to name your robot? ')
    while name == '':
        name = input('What do you want to name your robot? ')
    print(name + ': Hello kiddo!')
    return name


def turn_off_robot():
    """Turn off robot"""
    print('Shutting down..')


def print_list_commands(list_commands, list_explanation):
    """Print list of commands"""
    
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
    """Returns string of the output that will print when user enters help command"""
    
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


def set_direction_face(command, direction):
    """Sets direction robot faces after move"""
    
    index = 0
    coordinates = ['forward', 'back', 'right', 'left']
    
    if command == 'right' or command == 'left':        
        if command == 'right':
            if direction == 'forward':
                index += 2
            elif direction == 'right':
                index += 1
            elif direction == 'back':
                index += 3
        elif command == 'left':
            if direction == 'forward':
                index += 3
            elif direction == 'left':
                index += 1 
            elif direction == 'back':
                index += 2
        return coordinates[index]
    return direction


def get_coordinates(command, position, steps, direction):
    '''   F
          |
    L ----|---- R
          | 
          B
    '''
    if (direction == 'right' or direction == 'left'):
        index = 0
    else:
        index = 1
    if command == 'forward' and (direction != 'back' and direction != 'left'):
        position[index] += int(steps)
    elif command == 'back' or (command == 'forward' and (direction == 'back' or direction == 'left')):
        position[index] -= int(steps)
        
    return position


def move_robot_forward(steps, robot_info):
    """Moves robot forwards"""
    
    name = robot_info[0]
    position = robot_info[1]
    direction = robot_info[2]
    
    position = get_coordinates('forward', position, steps, direction)
    print(' > ' + str(name) + ' moved forward by ' + str(steps) + ' steps.')
    print(' > ' + str(name) + ' now at position ' + '(' + str(position[0]) + ',' + str(position[1]) + ')' +'.')


def move_robot_backwards(steps, robot_info):
    """Moves robot backwards"""
    
    name = robot_info[0]
    position = robot_info[1]
    direction = robot_info[2]
    
    position = get_coordinates('back', position, steps, direction)
    print(' > ' + str(name) + ' moved back by ' + str(steps) + ' steps.')
    print(' > ' + str(name) + ' now at position ' + '(' + str(position[0]) + ',' + str(position[1]) + ')' +'.')


def move_robot_right(robot_info):
    """Moves robot right"""
    
    name = robot_info[0]
    position = robot_info[1]
    direction = robot_info[2]
    
    position = get_coordinates('right', position, 'no_steps', direction)
    print(' > '+ str(name) +' turned right.')
    print(' > ' + str(name) + ' now at position ' + '(' + str(position[0]) + ',' + str(position[1]) + ')' +'.')


def move_robot_left(robot_info):
    """Moves robot left"""
    
    name = robot_info[0]
    position = robot_info[1]
    direction = robot_info[2]
    
    position = get_coordinates('left', position, 'no_steps', direction)
    print(' > '+ str(name) +' turned left.')
    print(' > ' + str(name) + ' now at position ' + '(' + str(position[0]) + ',' + str(position[1]) + ')' +'.')


def get_steps(command):
    """Calculates amount of steps from user's input"""
    
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
    """Returns move from user's input"""
    
    temp_num = 0
    move = ''
    for i in range(len(command)):
        try:
            temp_num = int(command[i])
            continue
        except:
            move = move + command[i]
    return move.lower().strip()


def turn_command_into_tuple(command):
    """format: (move, steps); if no steps are provided then steps = no_steps"""
    
    tup_command = (get_move(command), get_steps(command))
    return tup_command


def choose_command(command, list_commands):
    """Returns tuple with command and amount of steps; ONLY if it's a valid move"""
    
    user_input = tuple_command_and_steps[0]
    
    tuple_command_and_steps = turn_command_into_tuple(command.lower().strip())
    for item in list_commands:
        if item.lower() == user_input:
            return tuple_command_and_steps
    return ('not_option', 'no_steps')


def do_command(tuple_command_and_steps, list_commands, list_explanations, tuple_robot_info):
    """Executes user's command; returns whether robot should turn off"""
    
    command = tuple_command_and_steps[0]
    steps = tuple_command_and_steps[1]
    
    if  command == 'off':
        turn_off_robot()
        return True
    elif command == 'help':
        print_list_commands(list_commands, list_explanations)
    elif command == 'forward':
        move_robot_forward(steps, tuple_robot_info)
    elif command == 'back':
        move_robot_backwards(steps, tuple_robot_info)
    elif command == 'right':
        move_robot_right(tuple_robot_info)
    elif command == 'left':
        move_robot_left(tuple_robot_info)
    return False


def robot_start():
    """This is the entry function, do not change"""
    
    off = False
    position = [0,0]
    name = name_robot()
    direction = 'forward'
    list_commands = ['OFF', 'HELP', 'FORWARD', 'BACK', 'RIGHT', 'LEFT']
    list_explanations = ['Shut down robot', 'provide information about commands', 'move robot forward', 'move robot backwards', 'turns robot right', 'turns robot left']

    while not off:
        print(name + ': ', end = '')
        command = input('What must I do next? ')
        while choose_command(command, list_commands)[0] == 'not_option':
            print('Sorry, I did not understand ', end = '')
            print('\'' + command + '\'.')
            command = input('What must I do next? ')
        tuple_command_and_steps = choose_command(command, list_commands)
        direction = set_direction_face(tuple_command_and_steps[0], direction)
        tuple_robot_info = (name, position, direction)
        off = do_command(tuple_command_and_steps, list_commands, list_explanations, tuple_robot_info)


if __name__ == "__main__":
    robot_start()
