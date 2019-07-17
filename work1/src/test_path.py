from os import path, getcwd, chdir

def print_my_path():
    print('cwd:     {}'.format(getcwd()))
    print('__file__:{}'.format(__file__))
    print('abspath: {}'.format(path.abspath(__file__)))
    print('basename: {}'.format(path.basename(__file__)))
    print('\n')

print_my_path()
chdir("..")

print_my_path()
