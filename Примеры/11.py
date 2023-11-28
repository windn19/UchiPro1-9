from functools import total_ordering


@total_ordering
class Test:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value


print(Test(5) > Test(2))
