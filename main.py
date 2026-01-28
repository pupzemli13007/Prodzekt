def steadyGene(gene):
    n = len(gene)
    docelowa_ilosc = n // 4

    licznik = {}
    for litera in gene:
        if litera not in licznik:
            licznik[litera] = 0
        licznik[litera] += 1

    nadmiar = {}
    for litera in ['A', 'C', 'G', 'T']:
        if litera not in licznik:
            licznik[litera] = 0
        if licznik[litera] > docelowa_ilosc:
            nadmiar[litera] = licznik[litera] - docelowa_ilosc

    if len(nadmiar) == 0:
        return 0

    lewy = 0
    min_dlugosc = n + 1
    okno = {}

    for prawy in range(n):
        litera = gene[prawy]
        if litera not in okno:
            okno[litera] = 0
        okno[litera] += 1

        while lewy <= prawy:
            czy_ok = True
            for lit, ile in nadmiar.items():
                if lit not in okno or okno[lit] < ile:
                    czy_ok = False
                    break

            if czy_ok:
                dlugosc = prawy - lewy + 1
                if dlugosc < min_dlugosc:
                    min_dlugosc = dlugosc

                litera_lewa = gene[lewy]
                okno[litera_lewa] -= 1
                lewy += 1
            else:
                break

    return min_dlugosc