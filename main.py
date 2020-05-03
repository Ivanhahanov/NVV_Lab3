def show_table(table):
    for string in table:
        for elem in string:
            print(elem, end='\t')
        print()


def round_table(table):
    return [round(elem, 3) for elem in table]


def pretty_table(table):
    res = [[], [], [], []]
    n = 0
    for i in range(4):
        for j in range(4):
            res[i].append(table[j + n])
        n += 4
    return res


def table_T(table):
    return list(zip(*table))


# Входные значения
table_a = [[0.7, 0.7, 0.3, 0.8],
           [0.5, 1, 1, 0.5],
           [0.7, 0, 0, 1],
           [1, 0.6, 0.9, 0.5]]

table_b = [[1, 0.5, 0.6, 0.3],
           [0.5, 1, 1, 0.5],
           [0.4, 0, 1, 0.2],
           [0.7, 0.5, 0.8, 0.1]]

table_e = [[0, 0.5, 0.3, 0.2],
           [0.5, 0, 1, 0.5],
           [0.7, 0, 0, 0.9],
           [0.8, 0.5, 0.1, 0]]
table_r1 = list()
table_r2 = list()
for line in zip(table_a, table_b, table_e):
    for i, a, b, e in zip([num for num in range(16)], *line):
        r1 = min(max((1 - b), e), (1 - a)) # Формулы в зависимости от вариантов
        r2 = min(1 - (min(e, b)), (1 - a))
        table_r1.append(r1)
        table_r2.append(r2)

table_r1 = pretty_table(round_table(table_r1))
table_r1_T = table_T(table_r1)
table_r2 = pretty_table(round_table(table_r2))
table_r2_T = table_T(table_r2)
print('R1')
show_table(table_r1)
print('R2')
show_table(table_r2)

minmax = list()
for o_line in table_r1:
    for line, line2 in zip(o_line, table_r2_T):
        m = []
        n_line = list()
        for elem in zip(o_line, line2):
            m.append(min(elem))
        minmax.append(max(*m))
print("Maxmin")
show_table(pretty_table(minmax))

maxmin = list()
for o_line in table_r1:
    for line, line2 in zip(o_line, table_r2_T):
        m = []
        n_line = list()
        # print(n_line)
        for elem in zip(o_line, line2):
            # print(elem)
            m.append(max(elem))
        maxmin.append(min(*m))
print('Minmax')
show_table(pretty_table(maxmin))

multiple = list()
for o_line in table_r1:
    for line, line2 in zip(o_line, table_r2_T):
        m = []
        n_line = list()
        for a, b in zip(o_line, line2):
            m.append(a * b)
        multiple.append(max(*m))
print('Multiple')
show_table(pretty_table(round_table(multiple)))
