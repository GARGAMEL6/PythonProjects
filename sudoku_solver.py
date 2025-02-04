def algorithm_x(s: dict, y: dict, stack: list):
    if s == {}:
        return stack
    
    if y.values() == []:
        return []    
    

    for j in list(s.keys()):
        if len(s[j]) == min([len(value) for value in s.values()]):
            R = j
            break
    
    for X in s[R]:
        stack.append(X)
        buf = remove_columns(s, y, X)               #удаляем столбцы
        s1 = algorithm_x(s, y, stack)
        if s1 != []:
            return s1
        else:                                       #если решений нет -
            restore_columns(s, y, X, buf)           #возвращаем обратно
            stack.pop()
    return []


def restore_columns(columns: dict, rows: dict, base_row: str, buf: list):
    for el in rows[base_row][::-1]:
        columns[el] = buf.pop()
        for added_row in columns[el]:
            for col in rows[added_row]:
                columns[col].add(added_row)


def remove_columns(columns: dict, rows:dict, base_row):
    buf = []
    for el in rows[base_row]:
        buf.append(columns.pop(el))

        for intersecting_row in buf[-1]:
            for other_el in rows[intersecting_row]:
                if other_el != el:
                    columns[other_el].remove(intersecting_row)


    return buf





def xsudoku(A: list[list]):
    rows = dict()
    columns = dict()

    # в строки - ВСЕ возможные значения
    for row in range(1, 10):
        for col in range(1, 10):
            for num in range(1, 10):
                r = []
                quad = ((row - 1) // 3)*3 + (col - 1) // 3 + 1
                r += [(0, row, col), (1, row, num), (2, col, num), (3, quad, num)]
                rows[(row, col, num)] = r
    
    # в столбцы - пока что пустые множества
    for num in range(0, 4):
        for n1 in range(1, 10):
            for n2 in range(1, 10):
                columns[(num, n1, n2)] = set()
    
    print(len(rows))
    for i in range(729):
        rk, rv = list(rows.keys())[i], rows[list(rows.keys())[i]]
        for v in rv:
            columns[v].add(rk)
    

    s = []
    for i in range(9):
        for j in range(9):

            if A[i][j] > 0:
                el = (i+1, j+1, A[i][j])
                s.append(el)
                remove_columns(columns, rows, el)
    
    success = algorithm_x(columns, rows, s)
    if success == []:
        return []
    
    res = [[0 for j in range(9)] for i in range(9)]
    
    for (i, j, num) in s:
        res[i-1][j-1] = num
    
    return res




with open('sudoku.txt') as file:
    data = [[int(i) for i in x if i != '\n'] for x in file]
    
solved = xsudoku(data)

for i in range(9):
    for j in range(9):
        print(f' {solved[i][j]}', end='')
    print()

