#main-09/11
import generate_data
import run_query
from clickhouse_driver import Client  # Import the ClickHouse client
#import readyset


if __name__ == "__main__":
    # Define the number of rows for each table
    num_rows = 1000000000  # You can change this to 100,000,000 for the full dataset
		#  db_readyset = readyset.ReadySet()
	  db_clickhouse = ClickHouse()
    # Generate data for each table
    customer_df = generate_data.generate_customer_data(num_rows)
    lineorder_df = generate_data.generate_lineorder_data(num_rows)
    part_df = generate_data.generate_part_data(num_rows)
    supplier_df = generate_data.generate_supplier_data(num_rows)

    # Save the generated data to CSV files
    customer_df.to_csv('customer.csv', index=False)
    lineorder_df.to_csv('lineorder.csv', index=False)
    part_df.to_csv('part.csv', index=False)
    supplier_df.to_csv('supplier.csv', index=False)

    # Create a ClickHouse client to connect to your ClickHouse instance
    client = Client(host='127.0.0.1', port=9000, user='default', password='', database='default')

    # Run each query
    queries = [
        # Query 1.1
        """
        SELECT sum(LO_EXTENDEDPRICE * LO_DISCOUNT) AS revenue
        FROM lineorder_flat
        WHERE toYear(LO_ORDERDATE) = 1993 AND LO_DISCOUNT BETWEEN 1 AND 3 AND LO_QUANTITY < 25;
        """,

        # Query 1.2
        """
        SELECT sum(LO_EXTENDEDPRICE * LO_DISCOUNT) AS revenue
        FROM lineorder_flat
        WHERE toYYYYMM(LO_ORDERDATE) = 199401 AND LO_DISCOUNT BETWEEN 4 AND 6 AND LO_QUANTITY BETWEEN 26 AND 35;
        """,

        # Query 1.3
        """
        SELECT sum(LO_EXTENDEDPRICE * LO_DISCOUNT) AS revenue
        FROM lineorder_flat
        WHERE toISOWeek(LO_ORDERDATE) = 6 AND toYear(LO_ORDERDATE) = 1994
          AND LO_DISCOUNT BETWEEN 5 AND 7 AND LO_QUANTITY BETWEEN 26 AND 35;
        """,

        # Query 2.1
        """
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
        """,

        # Query 2.2
        """
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
        """,

        # Query 2.3
        """
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
        """,

        # Query 3.1
        """
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
        """,

        # Query 3.2
        """
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
        """,

        # Query 3.3
        """
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
        """,

        # Query 3.4
        """
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
        """,

        # Query 4.1
        """
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
        """,

        # Query 4.2
        """
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
        """,

        # Query 4.3
        """
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
    ]

    for i, query in enumerate(queries):
        print(f"Query {i + 1} Execution Time:", run_query.run_query(query, client))

    # Close the ClickHouse client
    client.disconnect()
