import sys


def main():
    # Uncomment this block to pass the first stage
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        # Wait for user input
        user_input = input()
        if user_input.split()[0] == 'exsit' and user_input.split()[1] == '0': break
        undefined_command(user_input)
    
def undefined_command(command):
    print(f"{command}: command not found")

if __name__ == "__main__":
    main()
