def partition(arr, left, right):
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


def quick_sort(arr, left, right):
    """
    Quick sort algoritam

    Argumenti:
    - `arr`: niz koji se sortira
    - `left`: indeks krajnjeg levog elementa
    - `right`: indeks krajnjeg desnog elementa
    """
    if left < right:
        pivot = partition(arr, left, right)
        quick_sort(arr, left, pivot - 1)
        quick_sort(arr, pivot + 1, right)
