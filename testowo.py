from enum import Enum
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    PINK = 4

indexes  = [1, 3, 4]
for i in indexes:
    print((Color(i).name))