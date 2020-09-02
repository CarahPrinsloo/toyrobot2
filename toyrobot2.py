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


def set_direction_face(direction_face, command):
    """Sets direction robot faces after move"""
    index = 0
    coordinates = ['forward', 'back', 'right', 'left']
            
    if command == 'right':
        if direction_face == 'forward':
            index += 2
        elif direction_face == 'right':
            index += 1
        elif direction_face == 'back':
            index += 3
    elif command == 'left':
        if direction_face == 'forward':
            index += 3
        elif direction_face == 'left':
            index += 1 
        elif direction_face == 'back':
            index += 2
    
    return coordinates[index]


def get_coordinates(command, position, direction_faces):
    '''   F
          |
    L ----|---- R
          | 
          B
    '''
    index = 0 if (direction_faces == 'right' or direction_faces == 'left') else index = 1
    if command = 'forward':
        position[index] += 1
    else:
        position[index] -= 1
    set_direction_face(direction_faces, command)
    return position


def move_robot_forward(name, steps, position):
    """Moves robot forwards"""
    
    position[1] = position[1] + int(steps)
    print(' > ' + str(name) + ' moved forward by ' + str(steps) + ' steps.')
    print(' > ' + str(name) + ' now at position ' + '(' + str(position[0]) + ',' + str(position[1]) + ')' +'.')


def move_robot_backwards(name, steps, position):
    """Moves robot backwards"""
    
    position[1] = position[1] - int(steps)
    print(' > ' + str(name) + ' moved back by ' + str(steps) + ' steps.')
    print(' > ' + str(name) + ' now at position ' + '(' + str(position[0]) + ',' + str(position[1]) + ')' +'.')


def move_robot_right(name, position):
    """Moves robot right"""
    
    print(' > '+ str(name) +' turned right.')
    print(' > ' + str(name) + ' now at position ' + '(' + str(position[0]) + ',' + str(position[1]) + ')' +'.')


def move_robot_left(name, position):
    """Moves robot left"""
    
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


def do_command(tuple_command, list_commands, list_explanations, name, position):
    """Executes user's command"""
    
    if  tuple_command[0] == 'off':
        turn_off_robot()
        return True
    elif tuple_command[0] == 'help':
        print_list_commands(list_commands, list_explanations)
    elif tuple_command[0] == 'forward':
        move_robot_forward(name, tuple_command[1], position)
    elif tuple_command[0] == 'back':
        move_robot_backwards(name, tuple_command[1], position)
    elif tuple_command[0] == 'right':
        move_robot_right(name, position)
    elif tuple_command[0] == 'left':
        move_robot_left(name, position)
    return False


def robot_start():
    """This is the entry function, do not change"""
    
    name = name_robot()
    off = False
    position = [0,0]
    list_commands = ['OFF', 'HELP', 'FORWARD', 'BACK', 'RIGHT', 'LEFT']
    list_explanations = ['Shut down robot', 'provide information about commands', 'move robot forward', 'move robot backwards', 'turns robot right', 'turns robot left']

    while not off:
        print(name + ': ', end = '')
        command = input('What must I do next? ')
        while choose_command(command, list_commands)[0] == 'not_option':
            print('Sorry, I did not understand ', end = '')
            print('\'' + command + '\'.')
            command = input('What must I do next? ')
        tuple_command = choose_command(command, list_commands)
        off = do_command(tuple_command, list_commands, list_explanations, name, position)


if __name__ == "__main__":
    robot_start()
