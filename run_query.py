#runquery -09/04
import time
import clickhouse_driver

# Function to run a query and measure execution time
def run_query(query, connection):
    start_time = time.time()
    cursor = connection.cursor()
    cursor.execute(query)
    cursor.fetchall()  # Fetching results to complete the query
    cursor.close()
    end_time = time.time()
    return end_time - start_time

if __name__ == "__main__":
    # Replace the connection details with your ClickHouse server information
    connection = clickhouse_driver.connect(
        host='127.0.0.1',
        port=9000,  # Default ClickHouse native port
        user='default',
        password='',
        database='default'
    )

    # Query 1.1
    q1_1 = """
    SELECT sum(LO_EXTENDEDPRICE * LO_DISCOUNT) AS revenue
    FROM lineorder_flat
    WHERE toYear(LO_ORDERDATE) = 1993 AND LO_DISCOUNT BETWEEN 1 AND 3 AND LO_QUANTITY < 25;
    """
    print("Query 1.1 Execution Time:", run_query(q1_1, connection))

    # Query 1.2
    q1_2 = """
    SELECT sum(LO_EXTENDEDPRICE * LO_DISCOUNT) AS revenue
    FROM lineorder_flat
    WHERE toYYYYMM(LO_ORDERDATE) = 199401 AND LO_DISCOUNT BETWEEN 4 AND 6 AND LO_QUANTITY BETWEEN 26 AND 35;
    """
    print("Query 1.2 Execution Time:", run_query(q1_2, connection))

    # Query 1.3
    q1_3 = """
    SELECT sum(LO_EXTENDEDPRICE * LO_DISCOUNT) AS revenue
    FROM lineorder_flat
    WHERE toISOWeek(LO_ORDERDATE) = 6 AND toYear(LO_ORDERDATE) = 1994
      AND LO_DISCOUNT BETWEEN 5 AND 7 AND LO_QUANTITY BETWEEN 26 AND 35;
    """
    print("Query 1.3 Execution Time:", run_query(q1_3, connection))

    # Query 2.1
    q2_1 = """
    SELECT
        sum(LO_REVENUE),
        toYear(LO_ORDERDATE) AS year,
        P_BRAND
    FROM lineorder_flat
    WHERE P_CATEGORY = 'MFGR#12' AND S_REGION = 'AMERICA'
    GROUP BY
        year,
        P_BRAND
    ORDER BY
        year,
        P_BRAND;
    """
    print("Query 2.1 Execution Time:", run_query(q2_1, connection))

    # Query 2.2
    q2_2 = """
    SELECT
        sum(LO_REVENUE),
        toYear(LO_ORDERDATE) AS year,
        P_BRAND
    FROM lineorder_flat
    WHERE P_BRAND >= 'MFGR#2221' AND P_BRAND <= 'MFGR#2228' AND S_REGION = 'ASIA'
    GROUP BY
        year,
        P_BRAND
    ORDER BY
        year,
        P_BRAND;
    """
    print("Query 2.2 Execution Time:", run_query(q2_2, connection))

    # Query 2.3
    q2_3 = """
    SELECT
        sum(LO_REVENUE),
        toYear(LO_ORDERDATE) AS year,
        P_BRAND
    FROM lineorder_flat
    WHERE P_BRAND = 'MFGR#2239' AND S_REGION = 'EUROPE'
    GROUP BY
        year,
        P_BRAND
    ORDER BY
        year,
        P_BRAND;
    """
    print("Query 2.3 Execution Time:", run_query(q2_3, connection))

    # Query 3.1
    q3_1 = """
    SELECT
        C_NATION,
        S_NATION,
        toYear(LO_ORDERDATE) AS year,
        sum(LO_REVENUE) AS revenue
    FROM lineorder_flat
    WHERE C_REGION = 'ASIA' AND S_REGION = 'ASIA' AND year >= 1992 AND year <= 1997
    GROUP BY
        C_NATION,
        S_NATION,
        year
    ORDER BY
        year ASC,
        revenue DESC;
    """
    print("Query 3.1 Execution Time:", run_query(q3_1, connection))

    # Query 3.2
    q3_2 = """
    SELECT
        C_CITY,
        S_CITY,
        toYear(LO_ORDERDATE) AS year,
        sum(LO_REVENUE) AS revenue
    FROM lineorder_flat
    WHERE C_NATION = 'UNITED STATES' AND S_NATION = 'UNITED STATES' AND year >= 1992 AND year <= 1997
    GROUP BY
        C_CITY,
        S_CITY,
        year
    ORDER BY
        year ASC,
        revenue DESC;
    """
    print("Query 3.2 Execution Time:", run_query(q3_2, connection))

    # Query 3.3
    q3_3 = """
    SELECT
        C_CITY,
        S_CITY,
        toYear(LO_ORDERDATE) AS year,
        sum(LO_REVENUE) AS revenue
    FROM lineorder_flat
    WHERE (C_CITY = 'UNITED KI1' OR C_CITY = 'UNITED KI5') AND (S_CITY = 'UNITED KI1' OR S_CITY = 'UNITED KI5') AND year >= 1992 AND year <= 1997
    GROUP BY
        C_CITY,
        S_CITY,
        year
    ORDER BY
        year ASC,
        revenue DESC;
    """
    print("Query 3.3 Execution Time:", run_query(q3_3, connection))

    # Query 3.4
    q3_4 = """
    SELECT
        C_CITY,
        S_CITY,
        toYear(LO_ORDERDATE) AS year,
        sum(LO_REVENUE) AS revenue
    FROM lineorder_flat
    WHERE (C_CITY = 'UNITED KI1' OR C_CITY = 'UNITED KI5') AND (S_CITY = 'UNITED KI1' OR S_CITY = 'UNITED KI5') AND toYYYYMM(LO_ORDERDATE) = 199712
    GROUP BY
        C_CITY,
        S_CITY,
        year
    ORDER BY
        year ASC,
        revenue DESC;
    """
    print("Query 3.4 Execution Time:", run_query(q3_4, connection))

    # Query 4.1
    q4_1 = """
    SELECT
        toYear(LO_ORDERDATE) AS year,
        C_NATION,
        sum(LO_REVENUE - LO_SUPPLYCOST) AS profit
    FROM lineorder_flat
    WHERE C_REGION = 'AMERICA' AND S_REGION = 'AMERICA' AND (P_MFGR = 'MFGR#1' OR P_MFGR = 'MFGR#2')
    GROUP BY
        year,
        C_NATION
    ORDER BY
        year ASC,
        C_NATION ASC;
    """
    print("Query 4.1 Execution Time:", run_query(q4_1, connection))

    # Query 4.2
    q4_2 = """
    SELECT
        toYear(LO_ORDERDATE) AS year,
        S_NATION,
        P_CATEGORY,
        sum(LO_REVENUE - LO_SUPPLYCOST) AS profit
    FROM lineorder_flat
    WHERE C_REGION = 'AMERICA' AND S_REGION = 'AMERICA' AND (year = 1997 OR year = 1998) AND (P_MFGR = 'MFGR#1' OR P_MFGR = 'MFGR#2')
    GROUP BY
        year,
        S_NATION,
        P_CATEGORY
    ORDER BY
        year ASC,
        S_NATION ASC,
        P_CATEGORY ASC;
    """
    print("Query 4.2 Execution Time:", run_query(q4_2, connection))

    # Query 4.3
    q4_3 = """
    SELECT
        toYear(LO_ORDERDATE) AS year,
        S_CITY,
        P_BRAND,
        sum(LO_REVENUE - LO_SUPPLYCOST) AS profit
    FROM lineorder_flat
    WHERE S_NATION = 'UNITED STATES' AND (year = 1997 OR year = 1998) AND P_CATEGORY = 'MFGR#14'
    GROUP BY
        year,
        S_CITY,
        P_BRAND
    ORDER BY
        year ASC,
        S_CITY ASC,
        P_BRAND ASC;
    """
    print("Query 4.3 Execution Time:", run_query(q4_3, connection))

    # Close the connection
    connection.disconnect()
