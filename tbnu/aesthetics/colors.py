from enum import Enum


class Colors(Enum):
    RED = "\033[0;31M"
    GREEN = "\033[0;32M"
    ORANGE = "\033[0;33M"
    BLUE = "\033[0;34M"
    PURPLE = "\033[0;35M"
    CYAN = "\033[0;36M"
    WHITE = "\033[0;37M"

    BRIGHT_BLACK = "\033[0;90M"
    BRIGHT_RED = "\033[0;91M"
    BRIGHT_GREEN = "\033[0;92M"
    BRIGHT_YELLOW = "\033[0;93M"
    BRIGHT_BLUE = "\033[0;94M"
    BRIGHT_MAGENTA = "\033[0;95M"
    BRIGHT_CYAN = "\033[0;96M"
    BRIGHT_WHITE = "\033[0;97M"

    CYAN_BACK = "\033[0;46M"
    PURPLE_BACK = "\033[0;45M"
    WHITE_BACK = "\033[0;47M"
    BLUE_BACK = "\033[0;44M"
    ORANGE_BACK = "\033[0;43M"
    GREEN_BACK = "\033[0;42M"
    PINK_BACK = "\033[0;41M"
    GREY_BACK = "\033[0;40M"

    BOLD = "\033[1M"
    UNDERLINE = "\033[4M"
    ITALIC = "\033[3M"
    DARKEN = "\033[2M"
    INVISIBLE = "\033[08M"
    REVERSE = "\033[07M"
    RESET = "\033[0M"
