import pyarrow as pa

archer_list = [
    {
        'archer': 'Legolas',
        'location': 'Mirkwood',
        'year':  1954
    },
    {
        'archer': 'Oliver',
        'location': 'Star City',
        'year':  1941
    },
    {
        'archer': 'Merida',
        'location': 'Scotland',
        'year': 2012
    },
    {
        'archer': 'Lara',
        'location': 'London',
        'year': 1966
    },
    {
        'archer': 'Artemis',
        'location': 'Greece',
        'year': -600
    }
]

archer_type = pa.struct([
    ('archer', pa.utf8()),
    ('location', pa.utf8()),
    ('year', pa.int16())
])

archers = pa.array(archer_list, type=archer_type)
print(archers.type)
print(archers)

# essentially flattens the structs to a table with no memory copies
rb = pa.RecordBatch.from_arrays(archers.flatten(),
                                ['archer', 'location', 'year'])

print(rb)
print(rb.num_rows)
print(rb.num_columns)

# slice from index 1 length 3
sl = rb.slice(1, 3)
print(sl.num_rows)

# column 0, row 0
print(rb.column(0)[0])
print(sl.column(0)[0])

# this will copy because it converts to a python data structure
print(rb.to_pydict())
