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
        
        self.hand = self.floor.pop(self.index)

    def __str__(self):
        return self.floor, self.hand