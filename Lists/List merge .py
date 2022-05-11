def combinar():
    lista1 = [1,2,5,6,9]
    lista2 = [3,4,7,8,10]

    print("La lista original 1 es: " + str(lista1))
    print("La lista original 2 es: " + str(lista2))

    size1 = len(lista1)
    size2 = len(lista2)

    res = []
    i, j = 0, 0

    while i < size1 and j < size2:
        if lista1[i] < lista2[j]:
            res.append(lista1[i])
            i += 1
        else:
            res.append(lista2[j])
            j += 1
    res = res + lista1[i:] + lista2[j:]
    print("La lista combinada ordenada es: " + str(res))