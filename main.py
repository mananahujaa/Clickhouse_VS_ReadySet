import generate_data
import run_query
#import readyset
#import clickhouse

if __name__ == "__main__":
  #data = generate_data.generate_data(100_000_000)
  data = generate_data.generate_data(10000)
#  db_readyset = readyset.ReadySet()
  db_clickhouse = ClickHouse()

  # Run simple queries
  query_simple = "SELECT * FROM data"
 # print("ReadySet:", run_query.run_query(query_simple, db_readyset))
  print("ClickHouse:", run_query.run_query(query_simple, db_clickhouse))

  # Run complex queries
  query_complex = "GROUP BY data, WHERE id = 1"
  #print("ReadySet:", run_query.run_query(query_complex, db_readyset))
  print("ClickHouse:", run_query.run_query(query_complex, db_clickhouse))
