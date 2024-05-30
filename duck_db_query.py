import duckdb
import pyarrow.parquet as pq

conn = duckdb.connect()

birthday_table = pq.read_table("data/birthdays.parquet")

results = conn.execute("SELECT * FROM birthday_table WHERE day < 20")
print(results.fetchall())
