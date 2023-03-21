class Entry:
    def __init__(self, priority, value):
        # Sets values self._priority and self._value
        self._priority = priority
        self._value = value

    def __str__(self):
        # Returns string in format
        return "Priority: {}; Value: {}".format(self._priority, self._value)

    def get_priority(self):
        # Returns priority of entry in list
        return self._priority

    def get_value(self):
        # Returns value of entry in list
        return self._value

    def set_priority(self, priority):
        # From parameter, it sets priority
        self._priority = priority
