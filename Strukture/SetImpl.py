class Set:
    def __init__(self):
        self._dict = {} #formira prazan recnik


    def add(self, item):
        """ dodaj jedan element u recnik. """
        if item not in self._dict.keys():
            self._dict[item] = item #dodaje novi element ako on vec ne postoji

    def remove(self, item):
        """ obrisi jedan element iz recnika. """
        del self._dict[item]

    def __len__(self):
        """ vrati duzinu recnika """
        return len(self._dict)


    def __or__(self, other):
        """Vraća novi skup kao uniju self i other."""
        result = Set() # rezultat je nova instanca
        for item in self._dict.keys():
            result.add(item) #dodaj item iz prvog recnika
        for item in other._dict.keys():
            result.add(item) #dodaj item iz drugog recnika
        return result

    def __and__(self, other):
        result = Set()  # rezultat je nova instanca
        for item in self._dict.keys():
            if item in other._dict.keys():
                result.add(item) #dodaj item samo ako se nalazi u oba recnika
        return result

    def __not__(self, other):
        result = Set()  # rezultat je nova instanca
        for item in self._dict.keys():
            if item not in other._dict.keys():
                result.add(item) #dodaj item samo ako se nalazi u prvom, a ne u drugom recniku
        return result

