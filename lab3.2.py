P = [['x','x','o'],
     ['o','x','x'],
     ['#','x','#']]
for row in P:
    if row.count('x') == 3:
        print('ДА')
for col in range(len(P)):
    column = [row[col] for row in P]
    if column.count('x') == 3:
        print('ДА')
d1 = [P[i][i] for i in range(len(P))]
if d1.count('x') ==3:
    print('ДА')
d2 = [P[i][len(P)-1-i] for i in range(len(P))]
if d2.count('x') == 3:
    print('ДА')

