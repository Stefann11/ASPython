def partition(dict, left, right):
    """
    Funkcija vrši particionisanje niza nad zadatim intervalom

    Particionisanje niza vrši se dovođenjem elemenata u takav
    redosled da su svi elementi manji ili jednaki pivotu levo
    od njega, dok se elementi veći od pivota dovode na pozicije
    desno od njega.

    Argumenti:
    - `arr`: niz koji se particioniše
    - `left`: indeks krajnjeg levog elementa
    - `right`: indeks krajnjeg desnog elementa
    """
    # poslednji element postaje pivot
    #pivot = arr[right]
    pivot = list(dict.values())[len(dict)-1]
    print("Pivot je ", pivot)

    # varijabla čuva indeks poslednjeg elementa manjeg od pivota
    i = left - 1
    print("I je ", i)

    '''
    for j in range(left, right):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    '''

    for j in range(left, right):
        print("Poredi: ", pivot, list(dict.values())[j])
        if list(dict.values())[j] <= pivot:

            i = i + 1
            print(i, j)
            
            list(dict.values())[i], list(dict.values())[j] = list(dict.values())[j], list(dict.values())[i]
            dict[list(dict)[i]], dict[list(dict)[right]] = dict[list(dict)[right]], dict[list(dict)[i]]


    i = i + 1
    #arr[i], arr[right] = arr[right], arr[i]

    list(dict.values())[i], list(dict.values())[right] = list(dict.values())[right], list(dict.values())[i]
    print(list(dict.values())[i], "       ", list(dict.values())[right])
    dict[list(dict)[i]], dict[list(dict)[right]] = dict[list(dict)[right]], dict[list(dict)[i]]
    print(list(dict.values())[i], "       ", list(dict.values())[right])
    return i


def quick_sort(dict, left, right):
    """
    Quick sort algoritam

    Argumenti:
    - `arr`: niz koji se sortira
    - `left`: indeks krajnjeg levog elementa
    - `right`: indeks krajnjeg desnog elementa
    """
    print(left, "    ", right)
    if left < right:
        pivot = partition(dict, left, right)
        quick_sort(dict, left, pivot - 1)
        quick_sort(dict, pivot + 1, right)

def wrap_quick_sort(arr):
    quick_sort(dict, 0, len(dict) - 1)

def getKeysByValue(dictOfElements, valueToFind):
    listOfItems = dictOfElements.items()
    for item  in listOfItems:
        if item[1] == valueToFind:
            return item[0]

def partition2(arr, left, right):
    """
    Funkcija vrši particionisanje niza nad zadatim intervalom

    Particionisanje niza vrši se dovođenjem elemenata u takav
    redosled da su svi elementi manji ili jednaki pivotu levo
    od njega, dok se elementi veći od pivota dovode na pozicije
    desno od njega.

    Argumenti:
    - `arr`: niz koji se particioniše
    - `left`: indeks krajnjeg levog elementa
    - `right`: indeks krajnjeg desnog elementa
    """
    # poslednji element postaje pivot
    pivot = arr[right]

    # varijabla čuva indeks poslednjeg elementa manjeg od pivota
    i = left - 1

    for j in range(left, right):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    i = i + 1
    arr[i], arr[right] = arr[right], arr[i]
    return i


def quick_sort2(arr, left, right):
    """
    Quick sort algoritam

    Argumenti:
    - `arr`: niz koji se sortira
    - `left`: indeks krajnjeg levog elementa
    - `right`: indeks krajnjeg desnog elementa
    """
    if left < right:
        pivot = partition2(arr, left, right)
        quick_sort2(arr, left, pivot - 1)
        quick_sort2(arr, pivot + 1, right)

    '''
    for index, (key, value) in enumerate(dict.items()):
        print(index, key, value)

    #dict[list(dict)[1]]=1333

    wrap_quick_sort(dict)

    for key, value in dict.items():
        print(key, value)
    '''
def sortiranje(dict):
    niz = []
    dict2 = {}

    for key, value in dict.items():
        niz.append(value)

    quick_sort2(niz, 0, len(niz)-1)

    for i in niz:
        for key, value in dict.items():
            if value == i:
                dict2[key] = value
    del dict[key]

    return dict2

if __name__ == "__main__":
    dict = {'A': 4, 'B': 77, 'C': 50, 'D': 50}

    dict = sortiranje(dict)

    for key, value in dict.items():
        print(key, value)
