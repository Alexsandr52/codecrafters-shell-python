import sys

def main():
    PATH = os.environ.get("PATH")
    builtin_commands = ["echo", "exit", "type"]

    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        # Wait for user input
        user_input = input().split()
        try:
            if user_input[0] == "exit" and user_input[1] == "0": break
            elif user_input[0] == "echo": print(" ".join(user_input[1:]))
            elif user_input[0] == 'type' and len(user_input) > 1: type_command(user_input[1]) 
            else: undefined_command(user_input[0])
        except: undefined_command(user_input[0])
    
def undefined_command(command):
    print(f"{command}: command not found")

def echo(input):
    print(input)

def type_command(command):
    
    command_path = None
    paths = PATH.split(":")
    
    for path in paths:
        if os.path.isfile(f"{path}/{command}"):
            command_path = f"{path}/{command}"
    
    if command in builtin_commands:
        sys.stdout.write(f"{command} is a shell builtin\n")
    elif command_path:
        sys.stdout.write(f"{command} is {command_path}\n")
    else:
        sys.stdout.write(f"{command} not found\n")

if __name__ == "__main__":
    main()
