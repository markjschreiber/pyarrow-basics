import pyarrow as pa
import numpy as np

NROWS = 8192
NCOLS = 16

data = [pa.array(np.random.randn(NROWS)) for i in range(NCOLS)]
cols = ['c' + str(i) for i in range(NCOLS)]
rb = pa.RecordBatch.from_arrays(data, cols)

print(rb.schema)
print(rb.num_rows)
