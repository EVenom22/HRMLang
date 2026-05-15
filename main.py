from commands import *

def read_program():
    with open("program.txt", "r") as file:
        prog: list[str] = file.readlines()
        for i in range(len(prog)):
            prog[i] = prog[i].split()
    return prog

if __name__ == "__main__":
    print("Thanks for using a0.1 HRMLang notbook version")

    program: list[str] = read_program()
    output: list = []
    while True:
        cmd: list[str] = program.pop(0)

        if "ENTRY" not in cmd:
            raise SyntaxError("Input can't be nothing")
        else:
            if len(cmd) != 3:
                raise SyntaxError("ENTRY command must have 2 arguments")
            else:
                try:
                    int(cmd[2])
                except ValueError:
                    raise SyntaxError("ENTRY command's second argument must be an integer")
                
                entry = ENTRY(cmd[1], int(cmd[2]))
                input: list[str] = entry.input
                floor: list = entry.floar
                break

    for i in range(len(program)):
        cmd: list[str] = program[i]

        if cmd == [] or cmd[0] == " " or cmd[0] == "ENTRY" or cmd[0] == "/":
            pass

        elif cmd[0] == "INBOX":
            command = INBOX(input)
            hand = command.input

        elif cmd[0] == "OUTBOX":
            if hand == None:
                raise SyntaxError("You can't place nothing in the OUTBOX")

            command = OUTBOX(hand, output)
            output = command.output
            hand = None
            
            if input == []:
                break
        
        elif cmd[0] == "COPYTO":
            if len(cmd) != 2:
                raise SyntaxError("COPYTO command must have 1 argument")
            else:
                command = COPYTO(hand, floor, int(cmd[1]))
                floor = command.floor

        elif cmd[0] == "COPYFROM":
            if len(cmd) != 2:
                raise SyntaxError("COPYFROM command must have 1 argument")
            else:
                command = COPYFROM(hand, floor, int(cmd[1]))
                floor = command.floor
                hand = command.hand
        
        else:
            raise SyntaxError("Unknow command")

    print(output)
