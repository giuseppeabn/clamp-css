

class ClampCss:
    def __init__(self, min_screen: int = 1366, max_screen: int = 1920, fontSize_base: int = 16, decimal: int = 2):
        self.min_screen = min_screen
        self.max_screen = max_screen
        self.fontSize_base = fontSize_base
        self.decimal = decimal

    def transform_value_to_rem(self, value):
        return f"{round(value / self.fontSize_base, self.decimal)}rem"

    def getClamp(self, min_size, max_size):
        v = round(((100 * (max_size - min_size)) /
                   (self.max_screen - self.min_screen)), self.decimal)
        r = ((self.min_screen * max_size) - (self.max_screen * min_size)
             ) / (self.min_screen - self.max_screen)

        return f"clamp({self.transform_value_to_rem(min_size)}, {v}vw + {self.transform_value_to_rem(r)}, {self.transform_value_to_rem(max_size)})"
