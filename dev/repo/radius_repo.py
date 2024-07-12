from repo.value_repo import ValueRepo
from services.log import info


class RadiusRepo(ValueRepo):
    entry = "FastFillet.Radius"
    value_type = float
    default_value = 0.25

    values = [
        0.1875,
        0.25,
        0.5,
        0.6,
        0.75,
        1,
        1.25,
        1.5,
        1.75,
        2,
        2.25,
        2.5,
        2.75,
        3,
        3.5,
        4,
        4.5,
        5,
    ]

    def factory(self, value_string):
        value = float(value_string)
        return value

    def destructor(self, value):
        str_value = str(max(value, 0.0))
        return str_value

    @property
    def index(self):
        # Get current value
        current_value = self.get()
        current_index = self.values.index(current_value)
        return current_index

    def up(self):
        next_index = min(self.index + 1, len(self.values) - 1)
        next_value = self.values[next_index]
        self.set(next_value)

    def down(self):
        next_index = max(self.index - 1, 0)
        next_value = self.values[next_index]
        self.set(next_value)

    def reset(self):
        self.set(self.default_value)


class DefaultRepo:
    default_value = None

    def reset(self):
        self.set(self.default_value)


radius_repo = RadiusRepo()
info("Current Fast Fillet Radius: {}".format(radius_repo.get()))
