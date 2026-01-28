def connectedCell(matrix):
    n = len(matrix)
    m = len(matrix[0])

    odwiedzone = []
    for i in range(n):
        wiersz = []
        for j in range(m):
            wiersz.append(False)
        odwiedzone.append(wiersz)

    max_rozmiar = 0

    def dfs(wiersz, kolumna):
        if wiersz < 0 or wiersz >= n or kolumna < 0 or kolumna >= m:
            return 0

        if odwiedzone[wiersz][kolumna] or matrix[wiersz][kolumna] == 0:
            return 0

        odwiedzone[wiersz][kolumna] = True
        rozmiar = 1

        # 8 kierunków (góra, dół, lewo, prawo i 4 przekątne)
        rozmiar += dfs(wiersz - 1, kolumna)  # góra
        rozmiar += dfs(wiersz + 1, kolumna)  # dół
        rozmiar += dfs(wiersz, kolumna - 1)  # lewo
        rozmiar += dfs(wiersz, kolumna + 1)  # prawo
        rozmiar += dfs(wiersz - 1, kolumna - 1)  # góra-lewo
        rozmiar += dfs(wiersz - 1, kolumna + 1)  # góra-prawo
        rozmiar += dfs(wiersz + 1, kolumna - 1)  # dół-lewo
        rozmiar += dfs(wiersz + 1, kolumna + 1)  # dół-prawo

        return rozmiar

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1 and not odwiedzone[i][j]:
                rozmiar_regionu = dfs(i, j)
                if rozmiar_regionu > max_rozmiar:
                    max_rozmiar = rozmiar_regionu

    return max_rozmiar