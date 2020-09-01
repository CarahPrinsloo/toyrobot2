
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


def list_output_print_command(list_commands, list_explanation):
    output = []
    i = 0
    for command in list_commands:
        space = 0
        output.append(command)
        while space < 6 - (len(command)-1):
            if space == 4 - (len(command)-1):
                output.append('-')
            else:
                output.append(' ')
            space += 1
        output.append(list_explanation[i])
        i += 1
    output.append('\n')


def choose_command(command, list_commands):
    lowercase_command = command.lower().strip()
    for item in list_commands:
        if item.lower() == lowercase_command:
            return item
    return 'not_option'


def do_command(command, list_commands, list_explanations):
    if command.lower().strip() == 'off':
        turn_off_robot()
        return True
    elif command.lower().strip() == 'help':
        print('I can understand these commands:')
        print_list_commands(list_commands, list_explanations)
    return False


def robot_start():
    """This is the entry function, do not change"""
    name = name_robot()
    off = False
    list_commands = ['OFF', 'HELP']
    list_explanations = ['Shut down robot', 'provide information about commands']

    while not off:
        print_name(name)
        command = input('What must I do next? ')
        while choose_command(command, list_commands) == 'not_option':
            print('Sorry, I did not understand ', end = '')
            print('\'' + command + '\'.')
            command = input('What must I do next? ')
        off = do_command(command, list_commands, list_explanations)


if __name__ == "__main__":
    robot_start()
