import sys

def main():
    # Uncomment this block to pass the first stage
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
    if command in ["echo", "exit", "type"]:
        print(f"{command} is a shell builtin")
    else:
        print(f"{command} not found")

if __name__ == "__main__":
    main()
