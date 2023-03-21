from Entry import Entry


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
