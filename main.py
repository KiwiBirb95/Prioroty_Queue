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


class PQ:
    def __init__(self):
        # Creates empty list for entries
        self.list = []

    def add(self, priority, value):
        # Uses parameters to create an entry which is then appended to list
        entry = Entry(priority, value)
        self.list.append(entry)

    def remove_min(self):
        if len(self.list) == 0:
            # Checks list to see if it is empty and if it is returns None
            return None

        min_entry = self.list[0]
        # If list is not empty then initializes min_entry to the first entry in the list

        for entry in self.list:
            # This iterates through the entire list comparing priorities of the current min_entry

            if entry.get_priority() < min_entry.get_priority():
                # If entry is found with lower priority it updates min_entry to point to entry
                min_entry = entry

        self.list.remove(min_entry)
        # Removes min_entry from list and returns min_entry
        return min_entry

    def set_priority(self, value, new_priority):
        # Takes parameters and if entry has specific values it will set priority to new_priority
        for entry in self.list:
            if entry.get_value() == value:
                entry.set_priority(new_priority)

    def size(self):
        # Returns length of list
        return len(self.list)


# Testing Code
pq = PQ()
pq.add(2, "Eat")
pq.add(0, "Study for CS 3035")
pq.add(3, "Sleep")
pq.add(1, "Maintain Personal Relationships")
pq.add(4, "Practice Good Personal Hygiene")
pq.set_priority("Practice Good Personal Hygiene", 2)
pq.set_priority("Eat", 4)

while pq.size() > 0:
    print(pq.remove_min())