class Set:
    def __init__(self, *args):
        self._dict = {}
        for arg in args:
            self.add(arg)

    def extend(self, args):
        """ Add several items at once. """
        for arg in args:
            self.add(arg)

    def add(self, key, value):
        """ Add one item to the set. """
        if key not in self._dict:
            self._dict[key] = value
        else:
            self._dict[key]+=value

    def remove(self, item):
        """ Remove an item from the set. """
        del self._dict[item]

    def contains(self, item):
        """ Check whether the set contains a certain item. """
        return self._dict.has_key(item)

    # High-performance membership test for Python 2.0 and later
    __contains__ = contains

    def __getitem__(self, index):
        """ Support the 'for item in set:' protocol. """
        return self._dict.keys(  )[index]

    def __iter__(self):
        """ Better support of 'for item in set:' via Python 2.2 iterators """
        return iter(self._dict.copy(  ))

    def __len__(self):
        """ Return the number of items in the set """
        return len(self._dict)

    def items(self):
        """ Return a list containing all items in sorted order, if possible """
        result = self._dict.keys(  )
        try: result.sort(  )
        except: pass
        return result

    def __copy__(self):
        return Set(self)

    def __or__(self, other):
        """Vraća novi skup kao uniju self i other."""
        result = Set() # rezultat je nova instanca
        for key, value in self._dict.items():
            result.add(key,value)
        for key, value in other._dict.items():
            result.add(key,value)
        return result

    def __and__(self, other):
        result = Set()  # rezultat je nova instanca
        for key, value in self._dict.items():
            if key in other._dict.keys():
                result.add(key, value)
        return result

    def __not__(self, other):
        result = Set()  # rezultat je nova instanca
        for key, value in self._dict.items():
            if key not in other._dict.keys():
                result.add(key, value)
        return result

