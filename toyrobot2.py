def name_robot():
    name = input('What do you want to name your robot? ')
    while name == '':
        name = input('What do you want to name your robot? ')
    print(name, end = '')
    print(': Hello kiddo!')
    return name

def choose_command(command):
    lowercase_command = command.lower().strip()
    if lowercase_command == 'off':
        return 'off'


def turn_off_robot():
    print('Shutting down..')


def robot_start():
    """This is the entry function, do not change"""
    name = name_robot()
    off = False
    while not off:
        
