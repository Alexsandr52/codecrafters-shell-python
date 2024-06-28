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
            else: undefined_command(user_input[0])
        except: undefined_command(user_input[0])
    
def undefined_command(command):
    print(f"{command}: command not found")

def echo(input):
    print(input)

if __name__ == "__main__":
    main()
