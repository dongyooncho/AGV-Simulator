class Node:
    def __init__(self, name_input, x_input, y_input):
        super().__init__()

        self.NUM = name_input
        self.X = x_input
        self.Y = y_input
        self.isCross = False