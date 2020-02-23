"""def partition(dict, left, right):

    Funkcija vrši particionisanje niza nad zadatim intervalom

    Particionisanje niza vrši se dovođenjem elemenata u takav
    redosled da su svi elementi manji ili jednaki pivotu levo
    od njega, dok se elementi veći od pivota dovode na pozicije
    desno od njega.

    Argumenti:
    - `arr`: niz koji se particioniše
    - `left`: indeks krajnjeg levog elementa
    - `right`: indeks krajnjeg desnog elementa

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
"""

"""def quick_sort(dict, left, right):
    
    Quick sort algoritam

    Argumenti:
    - `arr`: niz koji se sortira
    - `left`: indeks krajnjeg levog elementa
    - `right`: indeks krajnjeg desnog elementa
   
    print(left, "    ", right)
    if left < right:
        pivot = partition(dict, left, right)
        quick_sort(dict, left, pivot - 1)
        quick_sort(dict, pivot + 1, right)
"""
"""
def wrap_quick_sort(arr):
    quick_sort(dict, 0, len(dict) - 1)

def getKeysByValue(dictOfElements, valueToFind):
    listOfItems = dictOfElements.items()
    for item  in listOfItems:
        if item[1] == valueToFind:
            return item[0]

"""


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
    #poslednji element postaje pivot

    pivot = arr[right]

    #varijabla čuva indeks poslednjeg elementa manjeg od pivota
    i = left - 1

    #obican algoritam rastuceg sortiranja
    for j in range(left, right):
        if arr[j] <= pivot:     #ako je j-ti element iz niza manji ili jednak od pivota
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]     #zameni

    i = i + 1
    arr[i], arr[right] = arr[right], arr[i]     #zameni
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
    if dict == {}:
        return {}   #proveravamo da li je dict prazan
    niz = []        #formiramo pomocni niz
    dict2 = {}      #ovaj dict cemo vratiti

    for key, value in dict.items():
        niz.append(value)   #u pomocni niz smestamo vrednosti iz dicta koji nam je poslat

    quick_sort2(niz, 0, len(niz)-1)     #u quick_sort saljemo ceo pomocni niz

    #algoritam koji ce popuniti dict2 tako da bude sortiran
    for i in niz:   #idi po svakoj vrednosti pomocnog niza koji je sada sortiran
        for key, value in dict.items():     #i po svakom kljucu i vrednosti iz dicta koji nam je poslat
            if value == i:      #ako se vrednost iz dict-a i vrednost iz niza poklapaju
                dict2[key] = value      #u dict2(koji vracamo) smesti kljuc i vrednost iz dict


    return dict2        #vrati dict2


