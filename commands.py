class ENTRY():
    def __init__(self, input: str, floor: int):
        self.input: str = list(input)
        self.floor: int = floor
        self.floar: list = [None] * self.floor
    
    def __str__(self):
        return self.input, self.floar

class INBOX():
    def __init__(self, input: list[str]):
        value = input.pop(0).upper()

        try:
            self.input = int(value)
        except ValueError:
            self.input = value
    
    def __str__(self):
        return self.input

class OUTBOX():
    def __init__(self, hand, output: list):
        self.output = output
        self.output.append(hand)
    
    def __str__(self):
        return self.output
    
class COPYTO():
    def __init__(self, hand, floor: list, index: int):
        self.hand = hand
        self.floor = floor
        self.index = index
        
        if self.hand == None:
            raise RuntimeError("you can't copy nothing")
        if len(self.floor) <= self.index or self.index < 0:
            raise IndexError("Index out of range")

        self.floor[self.index] = self.hand

    def __str__(self):
        return self.floor

class COPYFROM():
    def __init__(self, hand, floor: list, index: int):
        self.hand = hand
        self.floor = floor
        self.index = index

        if len(self.floor) <= self.index or self.index < 0:
            raise IndexError("Index out of range")
        if self.floor[self.index] == None:
            raise RuntimeError("You can't copy nothing")
        
        self.hand = self.floor[self.index]

    def __str__(self):
        return self.floor, self.hand

class JUMP():
    def __init__(self, id: str, program: list):
        self.id = id
        self.program = program
        target = id + ":"

        for index, line in enumerate(program):
            if line == []:
                continue
            if line[0] == target:
                self.target = index
                return

        raise RuntimeError(f"Label '{id}' not found")

class JUMPZ():
    def __init__(self, id: str, program: list, index: int, hand = None):
        self.id = id
        self.program = program
        self.hand = hand
        self.index = index

        if type(self.hand) == int and self.hand == 0:
            self.target = JUMP(self.id, self.program).target
        else:
            self.target = self.index

class JUMPN():
    def __init__(self, id: str, program: list, index: int, hand = None):
        self.id = id
        self.program = program
        self.hand = hand
        self.index = index

        if type(self.hand) == int and self.hand < 0:
            self.target = JUMP(self.id, self.program).target
        else:
            self.target = self.index

class BUMPUP():
    def __init__(self, hand, floor: list, index: int):
        self.hand = hand
        self.floor = floor
        self.index = index

        self.hand = COPYFROM(self.hand, self.floor, self.index).hand
        try:
            self.hand = int(self.hand)
        except ValueError:
            pass
        else:
            self.hand += 1
        self.floor = COPYTO(self.hand, self.floor, self.index).floor

class BUMPDN():
    def __init__(self, hand, floor: list, index: int):
        self.hand = hand
        self.floor = floor
        self.index = index

        self.hand = COPYFROM(self.hand, self.floor, self.index).hand
        try:
            self.hand = int(self.hand)
        except ValueError:
            pass
        else:
            self.hand -= 1
        self.floor = COPYTO(self.hand, self.floor, self.index).floor