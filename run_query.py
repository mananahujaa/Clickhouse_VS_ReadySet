import random
import time
import clickhouse_driver

def generate_data(size):
    # Your implementation for generating data goes here.
    # This function is not provided in the original code snippet.
    # It should return the generated data as needed for your use case.
    pass

def run_query(query, connection):
    """Runs a query on the database and returns the execution time."""
    start_time = time.time()
    cursor = connection.cursor()
    cursor.execute(query)
    cursor.fetchall()  # Fetching results to complete the query
    cursor.close()
    end_time = time.time()
    return end_time - start_time

if __name__ == "__main__":
    data = generate_data(100_000_000)

    # Replace the connection details with your ClickHouse server information
    connection = clickhouse_driver.connect(
        host='127.0.0.1',
        port=9000,  # Default ClickHouse native port
        user='default',
        password='',
        database='default'
    )

    # Run simple queries
    query_simple = "SELECT * FROM data"
    print("ClickHouse:", run_query(query_simple, connection))

    # Run complex queries
    query_complex = "SELECT data, COUNT(*) FROM your_table WHERE id = 1 GROUP BY data"
    print("ClickHouse:", run_query(query_complex, connection))

    # Close the connection
    connection.disconnect()

