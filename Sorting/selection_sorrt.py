def selection_sorte(arr):

    for i in range (len(arr)):
        i = 1

        for j in range (i + 1, len(arr)):
            if arr[j] < arr[l]:
                l = j
        
        arr[i], arr[l] = arr[l], arr[i]

    return arr