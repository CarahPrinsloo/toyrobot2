def name_robot():
    """Name robot"""
    
    name = input('What do you want to name your robot? ')
    while name == '':
        name = input('What do you want to name your robot? ')
    print(name + ': Hello kiddo!')
    return name


def turn_off_robot(name):
    """Turn off robot"""

    print(str(name)+': Shutting down..')


def print_list_commands(list_commands, list_explanation):
    """Print list of commands"""
    
    print('I can understand these commands:')
    for i in range(2):
        command = list_commands[i]
        spaces = 7 - len(command)
        print(command, end ='')
        for j in range(spaces):
            if j == (4 - (len(command) - 1)):
                print('-', end = '')
            else:
                print(' ', end = '')
        print(list_explanation[i])
    for k in range(2, len(list_commands)):
        print(' ' + str(list_commands[k]) + ' - ' + str(list_explanation[k]))
    print()


def list_commands_output(list_commands, list_explanation):
    """Returns string of the output that will print when user enters help command"""
    
    output = 'I can understand these commands:\n'
    for i in range(2):
        command = list_commands[i]
        spaces = 7 - len(command)
        output = output + str(command)
        for j in range(spaces):
            if j == (4 - (len(command) - 1)):
                output = output + '-'
            else:
                output = output + ' '
        output = output + str(list_explanation[i]) + '\n'
    for k in range(2, len(list_commands)):
        output = output + str(list_commands[k]) + ' - ' + str(list_explanation[k])+'\n'
    output = output + '\n'
    return output


def change_value_in_tuple(tuple_obj, index, value):
    """Changes value in tuple at specified index"""
    
    list_obj = list(tuple_obj)
    list_obj[index] = value
    tuple_obj = tuple(list_obj)
    return tuple_obj


def in_limit(axis, index):
    """Check to see if coordinates are in the limit"""
    
    if (axis > 100 or axis < -100) and index == 0:
        return False
    if (axis > 200 or axis < -200) and index == 1:
        return False
    return True


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
    """Modify coordinates for when robot moves"""
    #choose axis that is changed by move
    if (direction == 'right' or direction == 'left'):
        index = 0
    else:
        index = 1
    
    axis = position[index]

    #add/subtract steps from axis
    if command == 'forward' and (direction != 'back' and direction != 'left'):
        axis += int(steps)
    elif (command == 'back' and direction != 'left') or (command == 'forward' and (direction == 'back' or direction == 'left')):
        axis -= int(steps)
    elif command == 'back' and direction == 'left':
        axis += int(steps)
    
    #check if change is valid
    if in_limit(axis, index):
        position = change_value_in_tuple(position, index, axis)

    return position


def print_sprint_move(is_valid, name, position, steps):
    """Print output after robot performs sprint move"""
    
    if (is_valid):
        for i in range(0, int(steps)):
            print_steps = int(steps) - i
            print(' > '+ str(name) +' moved forward by '+ str(print_steps) +' steps.')
    

def calculate_sprint_taken_steps(steps, name):
    """Calculate # steps taken by robot when sprint move is performed"""
    
    if (steps != 0):
        return steps + calculate_sprint_taken_steps(steps - 1, name)
    else:
        return steps


def sprint(steps, robot_info):
    """Perform sprint move"""

    name = robot_info[0]
    position = robot_info[1]
    direction = robot_info[2]
    
    temp_position = position
    taken_steps = calculate_sprint_taken_steps(int(steps), name)
    position = get_coordinates('forward', position, taken_steps, direction)
    print_sprint_move(temp_position != position, name, position, steps)
    robot_info = (name, position, direction)
    return robot_info
    

def move_robot(command, steps, robot_info):
    """Moves robot"""

    name = robot_info[0]
    position = robot_info[1]
    direction = robot_info[2]
    
    prev_position = position
    position = get_coordinates(command, position, steps, direction)
    #invalid move
    if (position == prev_position) and (command != 'left') and (command != 'right') and (int(steps) != 0):
        print(str(name) + ': Sorry, I cannot go outside my safe zone.')
        robot_info = (name, position, direction) 
    #valid move
    else:
        #forward/backwards
        if command != 'left' and command != 'right':
            print(' > ' + str(name) + ' moved '+ str(command) +' by ' + str(steps) + ' steps.')
        #left/right
        else:
            print(' > ' + name + ' turned '+ command + '.')
        direction = set_direction_face(command, direction)
        robot_info = (name, position, direction)
    return robot_info
    

def get_steps(command):
    """Returns # steps from input"""
    
    number = 0
    string_number = ''
    digits = 0
    for i in range(len(command)):
        try:
            number = int(command[i])
            string_number = string_number + command[i]
            digits += 1
        except:
            #invalid input for steps
            if digits > 0:
                string_number = ''
                break
            #not integer
            continue
    if len(string_number) == 0:
        return 'no_steps'
    return string_number


def get_move(command):
    """Returns move-type from input"""
    
    temp_number = 0
    move = ''
    digits = 0
    for i in range(len(command)):
        try:
            temp_number = int(command[i])
            digits += 1
        except:
            if digits == 0:
                move = move + command[i]
    return move.lower().strip()


def check_valid_input(command, steps):
    """Check if (valid) command has correct step input"""
    
    command_and_steps = (command, steps)
    if (command == 'back' or command == 'forward' or command == 'sprint') and steps == 'no_steps':
        command_and_steps = ('not_option', 'no_steps')
    elif (command == 'right' or command == 'left') and steps != 'no_steps':
        command_and_steps = ('not_option', 'no_steps')
    return command_and_steps
   

def choose_command(command, list_commands):
    """Returns tuple with command and # of steps; ONLY if it's a valid move"""
    
    command_input = get_move(command.lower().strip())
    for item in list_commands:
        if item.lower() == command_input:
            command_and_steps = check_valid_input(command_input, get_steps(command.lower().strip()))
            return command_and_steps
    return ('not_option', 'no_steps')


def do_command(tuple_command_and_steps, list_commands, list_explanations, robot_info):
    """Executes user's command; returns whether robot should turn off"""
    
    command = tuple_command_and_steps[0]
    steps = tuple_command_and_steps[1]
    name = robot_info[0]
    
    if command == 'help':
        print_list_commands(list_commands, list_explanations)
    else:
        if command == 'forward':
            robot_info = move_robot(command, steps, robot_info)
        elif command == 'back':
            robot_info = move_robot(command, steps, robot_info)
        elif command == 'right':
            robot_info = move_robot(command, steps, robot_info)
        elif command == 'left':
            robot_info = move_robot(command, steps, robot_info)
        elif command == 'sprint':
            robot_info = sprint(steps, robot_info)
        #print position after robot moved
        position = robot_info[1]
        print(' > ' + str(name) + ' now at position ' + '(' + str(position[0]) + ',' + str(position[1]) + ').')
    
    return robot_info


def robot_start():
    """This is the entry function, do not change"""
    
    position = (0,0)
    name = name_robot()
    direction = 'forward'
    robot_info = (name, position, direction)
    list_commands = ['OFF', 'HELP', 'FORWARD', 'BACK', 'RIGHT', 'LEFT', 'SPRINT']
    list_explanations = ['Shut down robot', 'provide information about commands', 'move robot forward', 'move robot backwards', 'turns robot right', 'turns robot left', 'gives the robot a short burst of speed and distance']

    while True:
        print(name + ': ', end = '')
        command = input('What must I do next? ')
        while choose_command(command, list_commands)[0] == 'not_option':
            print(str(name) + ': Sorry, I did not understand '+'\'' + str(command) + '\'.')
            command = input(str(name)+': What must I do next? ')
        if  command.lower().strip() == 'off':
            turn_off_robot(name)
            break
        command_and_steps = choose_command(command, list_commands)
        robot_info = do_command(command_and_steps, list_commands, list_explanations, robot_info)


if __name__ == "__main__":
    robot_start()
