def generujTabliceGeometrii(x0, xp, n):
    temp = (xp - x0) / (n - 1)
    matrix = np.array([x0])

    for i in range(1, n, 1):
        matrix = np.block([matrix, i * temp + x0])
    return matrix