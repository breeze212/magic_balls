def horse_chess(sz):
    place_chess = input()
    abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    x1 = int(place_chess[1])
    y1 = abc.index(place_chess[0])
    print(x1)
    print(y1)
    matrix = []
    # заполняем матрицуb6
    for i in range(sz):
        rows = ['.' for i in range(sz)]
        matrix.append(rows)
        #print(*rows)
    # перебираем возможные ходы коня
    for i in range(sz - 1, -1, -1):
        for j in range(sz - 1, -1, -1):
            if x1 == i and y1 == j:
                matrix[i][j] = 'N'
            if (x1 - i) ** 2 + (y1 - j) ** 2 == 5:
                matrix[i][j] = '*'
        print(*matrix[i])

size_table = 8
horse_chess(size_table)
