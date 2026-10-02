class Counter:
    def __init__(self, initial=0, min_value=0, max_value=10):
        self.min_value = min_value
        self.max_value = max_value
        self.value = initial

    def set_max(self, max_value):
        self.max_value = max_value

    def set_min(self, min_value):
        self.min_value = min_value

    def set_initial(self, initial):
        self.value = initial

    def step_up(self):
        if self.value >= self.max_value:
            raise ValueError("Досягнуто максимуму")
        self.value += 1

    def step_down(self):
        if self.value <= self.min_value:
            raise ValueError("Досягнуто мінімуму")
        self.value -= 1

    def get_current(self):
        return self.value



counter = Counter(5, 0, 10)

print(counter.get_current())

counter.step_up()
print(counter.get_current())

counter.step_down()
print(counter.get_current())