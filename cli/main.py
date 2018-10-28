
# CLI simulator in Python

bash_history = []   # to be used in later version using pickle or HDF5..


def run():
    while True:
        cmd = input('$ ')
        if 'exit' in cmd.lower():
            exit()


def main():
    init_string = '''
        Hello. This is a command line simulation.
        Type in 'exit' anytime to return to the shell.
        Enter the commands with a 'sh' before them to run them directly
        to the shell.
        Example:
            $ sh ls -l
        is the same as typing
            ls -l
        in the terminal.
        Here you go.
    '''
    print(init_string)
    run()


if __name__ == '__main__':
    main()
