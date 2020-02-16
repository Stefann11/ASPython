class Set:
    def __init__(self):
        self._dict = {}


    def add(self, item):
        """ Add one item to the set. """
        if item not in self._dict.keys():
            self._dict[item] = item

    def remove(self, item):
        """ Remove an item from the set. """
        del self._dict[item]

    def __len__(self):
        """ Return the number of items in the set """
        return len(self._dict)


    def __copy__(self):
        return Set(self)

    def __or__(self, other):
        """Vraća novi skup kao uniju self i other."""
        result = Set() # rezultat je nova instanca
        for item in self._dict.keys():
            result.add(item)
        for item in other._dict.keys():
            result.add(item)
        return result

    def __and__(self, other):
        result = Set()  # rezultat je nova instanca
        for item in self._dict.keys():
            if item in other._dict.keys():
                result.add(item)
                #result.add(key, other._dict[key])
        return result

    def __not__(self, other):
        result = Set()  # rezultat je nova instanca
        for item in self._dict.keys():
            if item not in other._dict.keys():
                result.add(item)
        return result

