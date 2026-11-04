

def get_input():
    usr_input = input("Please give me some input: ")
    return usr_input

def int_check(usr_input):
    if usr_input.isdigit():
        usr_input = int(usr_input)
        print(usr_input)
    else:
        print("That's not a number!!!!!!")
    
def main():
    captured_input = get_input()
    int_check(captured_input)
    
main()
