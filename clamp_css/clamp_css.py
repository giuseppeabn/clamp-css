

class _ClampCss:
    def __init__(self, min_screen: int = 1366, max_screen: int = 1920, fontSize_base: int = 16, decimal: int = 2):
        self.__min_screen = min_screen
        self.__max_screen = max_screen
        self.__fontSize_base = fontSize_base
        self.__decimal = decimal

    def get_min_screen(self):
        return self.__min_screen

    def get_max_screen(self):
        return self.__max_screen

    def get_fontSize_base(self):
        return self.__fontSize_base

    def get_decimal(self):
        return self.__decimal

    def transform_value_to_rem(self, value) -> str:
        return f"{round(value / self.__fontSize_base, self.__decimal)}rem"

    def get_clamp(self, min_size, max_size) -> str:
        v = round(((100 * (max_size - min_size)) /
                   (self.__max_screen - self.__min_screen)), self.__decimal)
        r = ((self.__min_screen * max_size) - (self.__max_screen * min_size)
             ) / (self.__min_screen - self.__max_screen)

        return f"clamp({self.transform_value_to_rem(min_size)}, {v}vw + {self.transform_value_to_rem(r)}, {self.transform_value_to_rem(max_size)})"
