import pyarrow as pa
import pyarrow.parquet as pq

days = pa.array([1, 12, 17, 23, 28], type=pa.int8())
months = pa.array([1, 3, 5, 7, 1], type=pa.int8())
years = pa.array([2000, 2014, 1995, 1999, 1995], type=pa.int16())

birthday_table = pa.table([days, months, years],
                          names=["day", "month", "year"])
print("Created table:")
print(birthday_table)
print()

# write to parquet
pq.write_table(birthday_table, "data/birthdays.parquet", compression="zstd")
parquet_file = pq.ParquetFile("data/birthdays.parquet")
print("wrote to parquet with metadata:")
print(parquet_file.metadata)
print()

# read from parquet
birthday_table_2 = pq.read_table("data/birthdays.parquet")
print("read from parquet:")
print(birthday_table_2)
