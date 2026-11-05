

# def get_input():
#   usr_input = input("Please give me some input: ")
#   return usr_input

def int_check(usr_input):
    if usr_input.isdigit():
        usr_input = int(usr_input)
        # print(usr_input)
        return usr_input
    else:
        usr_input = "That's not a number!!!!!!"
        return usr_input
    
def main():
    usr_input = input("Please give me some input: ")
    #captured_input = get_input()
    usr_input = int_check(usr_input)
    print(usr_input)
    
main()
