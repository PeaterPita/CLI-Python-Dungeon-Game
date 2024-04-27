from enum import Enum

class Color(Enum):
    BLACK = 1, "\033[90m"
    RED = 2, "\033[91m"
    GREEN = 3, "\033[92m"
    YELLOW = 4, "\033[93m"
    BLUE = 5, "\033[94m"
    MAGENTA = 6, "\033[95m"
    CYAN = 7, "\033[96m"
    WHITE = 8, "\033[97m"
    
    CLEAR = 99, "\033[0m"
    