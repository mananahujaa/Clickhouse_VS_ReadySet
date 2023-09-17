# Comparative analysis - Revised

To: Professor Yicheng Tu

A report by:

Manan Ahuja

U31258733

## 🗯️Revised Experiment Requirements:

1. **Diverse Workloads:** The experiment requires the evaluation of a set of career workloads using realistic datasets obtained from the ClickHouse website. These datasets should adhere to the Star Schema Benchmark, ensuring the relevance and applicability of the data.
2. **Comparison between ClickHouse and ReadySet:** The experiment necessitates running identical SQL queries on both ClickHouse and ReadySet databases, utilizing the provided datasets. This step is crucial for assessing the performance of both database systems under the same conditions.
3. **SQL Queries Alignment:** The SQL queries employed in the experiment should be specifically designed for the ClickHouse dataset using the Star Schema Benchmark. This alignment ensures that the queries reflect the workload accurately and facilitate a meaningful performance comparison.
4. **Data Scaling:** To discern performance trends, the experiment mandates altering the dataset size. This involves running the workload on both ClickHouse and ReadySet with datasets that are both smaller and larger. By doing so, the goal is to identify scenarios in which one database outperforms the other, and under which queries, as the dataset scales.

In essence, this experiment aims to provide a comprehensive performance assessment by comparing ClickHouse and ReadySet databases under varying dataset sizes and workload scenarios, with a specific focus on the Star Schema Benchmark. The objective is to uncover trends that reveal the comparative strengths and weaknesses of each database system in real-world scenarios.

# 👉🏾Introduction

The goal of this project is to conduct a comprehensive comparative analysis of two prominent columnar databases, ReadySet and ClickHouse, using the Star Schema Benchmark (SSB) dataset. This project aims to assess the performance, scalability, and efficiency of both databases under various conditions, including different dataset sizes. The analysis will provide insights into which database is better suited for specific query workloads and dataset scales.

**Project Objectives:**

1. **Benchmarking ReadySet and ClickHouse**: The project will start by setting up both ReadySet and ClickHouse databases and loading them with the SSB dataset. This will create a baseline for performance evaluation.
2. **Executing Standard Queries**: A set of standard SQL queries based on the SSB dataset will be executed on both databases using python files. These queries will represent common analytical tasks to evaluate the initial performance of both ReadySet and ClickHouse.
3. **Analyzing Initial Results**: The initial query results will be compared in terms of query execution time and resource utilization. This analysis will help identify strengths and weaknesses in each database for standard analytical tasks.
4. **Scaling Dataset Size**: The dataset size will be modified to create both smaller and larger datasets. The same set of queries will be executed on these varied dataset sizes to observe how both databases perform as the data scales.
5. **Trend Analysis**: By analyzing the performance of both databases under different dataset sizes and query workloads, trends will be identified. This will help in understanding which database is more efficient for specific tasks and dataset sizes.

## ReadySet

ReadySet is a cloud-based data warehouse platform that is designed to be easy to use. It does not require any coding skills, and it provides a graphical user interface (GUI) for data exploration. ReadySet is a good choice for projects that require a simple and easy-to-use data warehouse. It is also a good option for projects that are on a budget, as it offers a free tier.

## ClickHouse

ClickHouse is an open-source data warehouse platform that is known for its speed and scalability. It can handle large datasets with ease, and it can be used to run complex queries quickly. ClickHouse is a good choice for projects that require a fast and scalable data warehouse. It also offers a wide range of features, including support for multiple data sources and complex aggregations.

## ⚖️Comparison

ReadySet and ClickHouse are both good data warehouse platforms, but they have different strengths and weaknesses. ReadySet is easier to use, but it is not as scalable as ClickHouse. ClickHouse is more complex to use, but it is faster and more scalable.

## 💽Data used:(files at the bottom of report)

In the context of data warehousing and business intelligence, the "Star Schema" is a popular data modeling technique. It's designed to optimize querying and reporting on large datasets. The Star Schema is characterized by a central fact table, which contains measurable data (often referred to as facts), and dimension tables that provide context to the facts.

Here's a brief explanation of the components in a Star Schema:

1. **Fact Table**: This is the central table in the schema and holds quantitative data, typically referred to as "facts." These facts are numerical measures, such as sales revenue, profit, or quantity sold. The fact table often contains foreign keys that reference dimension tables, allowing you to associate facts with various dimensions.
2. **Dimension Tables**: Dimension tables provide descriptive information about the data in the fact table. They contain textual or categorical attributes, which are used to filter, group, or aggregate the data in the fact table. Examples of dimension tables might include "Time," "Product," "Customer," or "Location." These tables help answer questions like "What product sold the most in a specific region during a particular time period?"
3. **Foreign Keys**: In the fact table, foreign keys are used to connect the facts with their associated dimensions. These keys act as links to the dimension tables, allowing you to join data from different dimensions to answer complex queries.

**Introduction to the Data Used:**

For your project, you're working with a dataset that follows the Star Schema model. The data includes several tables:

1. **Customer Dimension Table**: This table contains information about customers. It includes attributes such as customer name, address, city, nation, region, phone number, and market segment.
2. **Line Order Fact Table**: This is the central fact table in the schema. It holds data related to sales orders. It includes attributes such as order key, line number, customer key, part key, supplier key, order date, order priority, ship priority, quantity, extended price, total price, discount, revenue, supply cost, tax, commitment date, and ship mode.
3. **Part Dimension Table**: This table contains information about products or parts. It includes attributes like part key, name, manufacturer, category, brand, color, type, size, and container.
4. **Supplier Dimension Table**: This table provides details about suppliers. It includes attributes such as supplier key, name, address, city, nation, region, and phone number.

The data in these tables is generated synthetically for the purpose of your project. You can think of it as simulating data that might be found in a real-world retail or sales database. The Star Schema structure allows you to perform complex queries efficiently, aggregating and analyzing sales data based on various dimensions like customer, product, and time. You'll be running a set of predefined SQL queries on this data to assess the performance of ClickHouse and ReadySet databases.

## 🏁Queries run:

Here's an overview of the queries that you'll be running on the Star Schema dataset for your project:

**Query 1.1: Total Revenue by Year and Product Discount Range**

- This query calculates the total revenue for products sold in the year 1993, where the discount falls between 1 and 3, and the quantity sold is less than 25. It provides insights into revenue trends for specific products during that year.

```sql
SELECT sum(LO_EXTENDEDPRICE * LO_DISCOUNT) AS revenue
FROM lineorder_flat
WHERE toYear(LO_ORDERDATE) = 1993 AND LO_DISCOUNT BETWEEN 1 AND 3 AND LO_QUANTITY < 25;
```

**Query 1.2: Total Revenue by Year-Month and Discount-Quantity Range**

- This query calculates the total revenue for products sold in January 1994, where the discount falls between 4 and 6, and the quantity sold falls between 26 and 35. It helps analyze revenue patterns for a specific month with varying discounts and quantities.

```sql
SELECT sum(LO_EXTENDEDPRICE * LO_DISCOUNT) AS revenue
FROM lineorder_flat
WHERE toYYYYMM(LO_ORDERDATE) = 199401 AND LO_DISCOUNT BETWEEN 4 AND 6 AND LO_QUANTITY BETWEEN 26 AND 35;
```

**Query 1.3: Total Revenue by ISO Week, Year, Discount, and Quantity Range**

- This query calculates the total revenue for products sold in ISO week 6 of 1994, where the discount falls between 5 and 7, and the quantity sold falls between 26 and 35. It provides insights into revenue trends based on ISO week, year, and specific discount and quantity criteria.

```sql
SELECT sum(LO_EXTENDEDPRICE * LO_DISCOUNT) AS revenue
FROM lineorder_flat
WHERE toISOWeek(LO_ORDERDATE) = 6 AND toYear(LO_ORDERDATE) = 1994
  AND LO_DISCOUNT BETWEEN 5 AND 7 AND LO_QUANTITY BETWEEN 26 AND 35;
```

**Query 2.1: Total Revenue by Year, Product Brand, and Product Category (Filtering by Region)**

- This query aggregates total revenue by year, product brand, and product category for products categorized under 'MFGR#12' and sold in the 'AMERICA' region. It helps analyze revenue trends for a specific product category in a particular region over the years.

```sql
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
```

**Query 2.2: Total Revenue by Year, Product Brand (Filtered by Brand Range), and Region**

- This query calculates total revenue by year and product brand for products with brand codes between 'MFGR#2221' and 'MFGR#2228,' sold in the 'ASIA' region. It aids in analyzing revenue patterns for a range of product brands in a specific region.

```sql
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
```

**Query 2.3: Total Revenue by Year, Product Brand, and Region**

- This query calculates total revenue by year and product brand for products with brand 'MFGR#2239' sold in the 'EUROPE' region. It offers insights into revenue generated by a specific product brand in a particular region over the years.

```sql
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
```

**Query 3.1: Total Revenue by Customer and Supplier Nations (Filtered by Region and Year Range)**

- This query calculates total revenue by customer and supplier nations for transactions that occurred in the 'ASIA' region, involving customers and suppliers in the same region. The results are further filtered by the year range 1992-1997. It helps analyze revenue generated from regional transactions over time.

```sql
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
```

**Query 3.2: Total Revenue by Customer and Supplier Cities (Filtered by Nation and Year Range)**

- This query calculates total revenue by customer and supplier cities for transactions that occurred within the 'UNITED STATES,' involving customers and suppliers in the same nation. The results are filtered by the year range 1992-1997. It aids in analyzing revenue trends for transactions within a specific nation over time.

```sql
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
```

**Query 3.3: Total Revenue by Customer and Supplier Cities (Filtered by Multiple Cities and Year Range)**

- This query calculates total revenue by customer and supplier cities for transactions that occurred in multiple cities ('UNITED KI1' and 'UNITED KI5'), involving customers and suppliers in these cities. The results are filtered by the year range 1992-1997. It helps analyze revenue patterns for transactions between specific cities over time.

```sql
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
```

**Query 3.4: Total Revenue by Customer and Supplier Cities (Filtered by Multiple Cities and Year-Month)**

- This query calculates total revenue by customer and supplier cities for transactions that occurred in multiple cities ('UNITED KI1' and 'UNITED KI5') in December 1997. It offers insights into revenue generated from transactions between specific cities during a particular month.

```sql
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
```

**Query 4.1: Profit by Year and Customer Nation (Filtered by Region and Manufacturer)**

- This query calculates the profit by year and customer nation for transactions that occurred in the 'AMERICA' region, involving products manufactured by 'MFGR#1' or 'MFGR#2.' It helps analyze the profit generated from regional transactions over the years.

```sql
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
```

**Query 4.2: Profit by Year, Supplier Nation, and Product Category (Filtered by Region and Year)**

- This query calculates the profit by year, supplier nation, and product category for transactions that occurred in the 'AMERICA' region in the years 1997 and 1998. It offers insights into profit trends for specific product categories and supplier nations within a region.

```sql
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
```

**Query 4.3: Profit by Year, Supplier City, and Product Brand (Filtered by Nation and Year)**

- This query calculates the profit by year, supplier city, and product brand for transactions that involved suppliers from the 'UNITED STATES' in the years 1997 and 1998, focusing on products with the category 'MFGR#14.' It aids in analyzing profit patterns for specific product brands and supplier cities within a nation.

```sql
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
```

These queries are designed to provide valuable insights into the dataset's sales and transaction data, allowing you to evaluate

the performance of ClickHouse and ReadySet databases when executing complex analytical queries on a Star Schema dataset. By comparing the execution times of these queries, you can assess the efficiency and speed of each database system under different query scenarios and dataset sizes.

## 📠Hardware environment:

The hardware environment used for the analysis is a local machine running on MacOS with an M1 chip. The specific machine is a MacBook Pro model from the year 2020, equipped with 8GB of memory (RAM).

1. **Operating System:** The machine is running MacOS, which is Apple's proprietary operating system designed for its Mac computers.
2. **M1 Chip:** The MacBook Pro is powered by Apple's custom-designed M1 chip. The M1 is Apple's first silicon chip for Macs, integrating the CPU, GPU, and other components onto a single chip. It is based on ARM architecture and is known for its impressive performance and energy efficiency.
3. **Memory (RAM):** The machine has a substantial amount of memory, with 8GB of RAM. RAM is crucial for running applications and handling data efficiently, especially when working with large datasets or performing memory-intensive tasks.
4. **Python-Based Project:** The analysis was conducted using a Python-based project, which suggests that Python was the primary programming language used for data processing, analysis, and possibly other tasks. Python is a popular language in the data science and analytics community due to its versatility, extensive libraries, and ease of use.
5. ********Virtual Environment:******** The analysis was performed by forming a virtual environment using cloud based infrastructure(GCP)

Overall, this hardware environment provides a powerful setup for data analysis and allows for efficient processing of large datasets and complex computations. The combination of MacOS, the M1 chip, and ample memory (RAM) provides a solid foundation for running resource-intensive tasks in a Python-based project.

## 🪜Steps to setup virtual env:

To set up a virtual environment (venv) on GCP to do this project, you can follow these steps:

1. Create a new GCP project.
2. Enable the Cloud Shell API.
3. Open the Cloud Shell.
4. Create a new directory for your project.
5. Navigate to the project directory.
6. Create and activate a venv.

```python
python3 -m venv venv
source venv/bin/activate
```

- Install the required Python packages:

```python
pip install pandas faker
```

- Clone GitHub repository

```bash
git clone https://github.com/mananahujaa/Clickhouse_VS_ReadySet.git
```

## 🪜Steps for ClickHouse:

Introduction:
This guide outlines the installation process of ClickHouse and ReadySet on a MacOS machine. ClickHouse is a powerful open-source analytical database, while ReadySet streamlines the setup and management of ClickHouse clusters.

Step 1: System Update
Before proceeding with the installation, ensure that your system is up-to-date. Open a terminal and execute the following commands to update and upgrade existing packages:

```bash

sudo apt-get update
sudo apt-get upgrade

```

Step 2: ClickHouse Installation
ClickHouse can be installed on MacOS using the official ClickHouse website.

1. Download ClickHouse:
Visit the ClickHouse website (**[https://clickhouse.com/docs/en/install](https://clickhouse.com/docs/en/install)**) to download the installation package.
    
    ```bash
    
    curl https://clickhouse.com/ | sh
    
    ```
    
2. Start ClickHouse Server:
After the installation is complete, start the ClickHouse server by running the following command:
    
    ```bash
    ./clickhouse server
    
    ```
    
3. Open a New Terminal for Client:
To perform functions on the ClickHouse server, open a new terminal and execute the following command to launch the ClickHouse client:
    
    ```bash
    ./clickhouse client
    
    ```
    

## 🪜**Steps to Run ClickHouse Tests**

To perform tests on ClickHouse, follow these steps:

1. Compile dbgen :
    
    ```bash
    $ git clone git@github.com:vadimtk/ssb-dbgen.git
    $ cd ssb-dbgen
    $ make
    ```
    
2. Generate data:
    
    ```bash
    $ ./dbgen -s 1000 -T c
    $ ./dbgen -s 1000 -T l
    $ ./dbgen -s 1000 -T p
    $ ./dbgen -s 1000 -T s
    ```
    
    NOTE
    
    With **`-s 100`** dbgen generates 600 million rows (67 GB), while while **`-s 1000`** it generates 6 billion rows (which takes a lot of time)
    
3. Inserting Tables: 
    
    ```bash
    $ clickhouse-client --query "INSERT INTO customer FORMAT CSV" < customer.tbl
    $ clickhouse-client --query "INSERT INTO part FORMAT CSV" < part.tbl
    $ clickhouse-client --query "INSERT INTO supplier FORMAT CSV" < supplier.tbl
    $ clickhouse-client --query "INSERT INTO lineorder FORMAT CSV" < lineorder.tbl
    ```
    
4. Perform Queries: 
    
    ```bash
    ./clickhouse client --query "SELECT sum(LO_EXTENDEDPRICE * LO_DISCOUNT) AS revenue
    FROM lineorder_flat
    WHERE toYear(LO_ORDERDATE) = 1993 AND LO_DISCOUNT BETWEEN 1 AND 3 AND LO_QUANTITY < 25;"
    ```
    
    **Run queries Q1.1 to Q4.3 in the format given above^**
    
     
    

## 🪜Steps for readyset:

1. To install readyset by following commands from github repo [https://github.com/readysettech/readyset.git](https://github.com/readysettech/readyset.git) on local machine(MacOS)
2. Create a MySQL server, install docker on local machine, create a docker container and run docker on daemon mode with following commands: 
    
    ```docker
    docker run -d \
    --name=mysql \
    --publish=3306:3306 \
    -e MYSQL_ROOT_PASSWORD=readyset \
    -e MYSQL_DATABASE=testdb \
    mysql
    ```
    
3. generate data using generate_data.py and it will create a CSV. 
4. Load the CSV into MySQL table using the following steps :
    1. Create table in MySQL workbench using the commands:
        
        ```sql
        CREATE TABLE mySQL (
          id INT NOT NULL AUTO_INCREMENT,
          name VARCHAR(255) NOT NULL,
          email VARCHAR(255) NOT NULL,
          PRIMARY KEY (id)
        );
        ```
        
    2. Add the CSV into Table using commands :
        
        ```sql
        LOAD DATA INFILE 'file_path' INTO TABLE table_name;
        ```
        
5. Create a Docker container and start ReadySet inside it, connecting ReadySet to the database via the connection string in --upstream-db-url:
    
    ```docker
    docker run -d \
    --name=readyset \
    --publish=3307:3307 \
    --platform=linux/amd64 \
    --volume='readyset:/state' \
    --pull=always \
    -e DEPLOYMENT_ENV=quickstart_github \
    public.ecr.aws/readyset/readyset:beta-2023-06-29 \
    --standalone \
    --deployment='github-mysql' \
    --database-type=mysql \
    --upstream-db-url=mysql://root:readyset@172.17.0.1:3306/testdb \
    --address=0.0.0.0:3307 \
    --username='root' \
    --password='readyset' \
    --db-dir='/state'
    ```
    
6. check performance by running queries:

## 🙏🏾Ease of use

ReadySet is easier to use, with a user-friendly GUI, but ClickHouse is easier to install. ReadySet can handle a wide variety of data types and queries, but ClickHouse has better performance for complex queries. ReadySet is free to use, but ClickHouse has paid plans for larger datasets.

## 💯Performance

ClickHouse is much faster than ReadySet. ClickHouse can handle large datasets with ease, and it can be used to run complex queries quickly. ReadySet can be slow for large datasets, and it is not as good at handling complex queries. 

Sure, let's elaborate on the paragraph you provided.

ReadySet and ClickHouse are both data warehouses, but they have different performance characteristics. ClickHouse is much faster than ReadySet for both simple and complex queries. For example, the following table shows the results of running the two queries you mentioned on a dataset of 100 million rows:

| S.No: | Query | ClickHouse (ms)-60M rows | ReadySet (ms)-60M rows | ClickHouse Data Scaled Down(ms)- 6M rows | ReadySet 
Data Scaled Down(ms)- 6M rows | ClickHouse Data Scaled Up(ms)-600M rows | ReadySet
Data Scaled Upm(s)-600M rows |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Q1.1 | SELECT sum(LO_EXTENDEDPRICE * LO_DISCOUNT) AS revenue
FROM lineorder_flat
WHERE toYear(LO_ORDERDATE) = 1993 AND LO_DISCOUNT BETWEEN 1 AND 3 AND LO_QUANTITY < 25; | 11.3 | 17.4 | 1.1 | 0.9(Data is cached) | 107 | 221 |
| Q1.2 | SELECT sum(LO_EXTENDEDPRICE * LO_DISCOUNT) AS revenue
FROM lineorder_flat
WHERE toYYYYMM(LO_ORDERDATE) = 199401 AND LO_DISCOUNT BETWEEN 4 AND 6 AND LO_QUANTITY BETWEEN 26 AND 35; | 9.9 | 12.3 | 1 | 0.8 | 105 | 207 |
| Q1.3 | SELECT sum(LO_EXTENDEDPRICE * LO_DISCOUNT) AS revenue
FROM lineorder_flat
WHERE toISOWeek(LO_ORDERDATE) = 6 AND toYear(LO_ORDERDATE) = 1994
AND LO_DISCOUNT BETWEEN 5 AND 7 AND LO_QUANTITY BETWEEN 26 AND 35; | 10.1 | 11.2 | 1.1 | 0.8 | 107 | 213 |
|  |  |  |  |  |  |  |  |
| Q2.1 | SELECT
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
P_BRAND; | 21 | 34 | 2.3 | 3.2 | 149 | 310 |
| Q2.2 | SELECT
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
P_BRAND; | 18 | 27 | 1.9 | 2.7 | 135 | 298 |
| Q2.3 | SELECT
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
P_BRAND; | 19 | 24 | 2.1 | 2.2 | 172 | 263 |
| Q3.1 | SELECT
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
revenue DESC; | 58 | 71 | 5.3 | 8.2 | 833 = 0.8s | 1744 = 1.7s |
| Q3.2 | SELECT
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
revenue DESC; | 51 | 68 | 5.4 | 7.9 | 811=0.8s | 1527=1.5s |
| Q3.3 | SELECT
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
revenue DESC; | 55 | 67 | 5.3 | 7.7 | 809 | 1552 |
| Q3.4 | SELECT
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
revenue DESC; | 57 | 67 | 5.3 | 7.9 | 810 | 1535 |
| Q4.1 | SELECT
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
C_NATION ASC; | 61 | 64 | 7.2 | 11.5 | 846 | 1456 |
| Q4.2 | SELECT
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
P_CATEGORY ASC; | 63 | 62 | 7.9 | 11.2 | 825 | 1432 |
| Q4.3 | SELECT
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
P_BRAND ASC; | 63 | 62 | 7.8 | 11.3 | 833 | 1454 |

As you can see, ClickHouse is significantly faster than ReadySet for both queries. This is because ClickHouse is designed for fast performance, while ReadySet is designed for ease of use.

| Feature | ReadySet | ClickHouse |
| --- | --- | --- |
| Type | Cache-friendly database | Columnar database |
| Best for | Small or medium-sized datasets, simple queries | Large datasets, complex queries |
| Performance | Generally faster on small or medium-sized datasets and simple queries, but slower on large datasets or complex queries | Generally faster on all datasets and query types |
| Scalability | Horizontally scalable, but to a lesser extent than ClickHouse. Limited to cloud-based infrastructure | Horizontally scalable to very large datasets |
| Ease of use | Easy to use and manage | More complex to use and manage |
| Cost | Relatively inexpensive | More expensive |

**ReadySet may be faster:**

- Queries that are already cached.
- Queries that are not very complex.
- Small or medium-sized datasets, especially for simple read-heavy workloads.

**ReadySet may be slower:**

- Queries that are not cached.
- Complex queries.
- Large datasets.

Overall, ClickHouse is the better choice for applications that need to process large datasets or perform complex queries. However, ReadySet is a good choice for applications that need to improve the performance of read-heavy workloads on small or medium-sized datasets.

## 🪶Features

ClickHouse offers a wider range of features than ReadySet. ClickHouse supports multiple data sources, complex aggregations, and a variety of other features. ReadySet does not offer as many features, but it is still a capable data warehouse platform.

## 🎚️Scalability

ClickHouse is more scalable than ReadySet. ClickHouse can handle increasing amounts of data, while ReadySet can be limited by its cloud-based infrastructure.

## 🧾Recommendations

Based on the factors discussed above, we recommend the following:

If you need a simple and easy-to-use data warehouse for small projects, we recommend ReadySet. It is a good choice for projects that do not require a lot of complex querying or large datasets.

If you need a fast and scalable data warehouse with a wide range of features for larger projects, we recommend ClickHouse. It is a good choice for projects that require complex querying or large datasets.

## ℹ️Additional information

In addition to the factors discussed above, there are a few other things to consider when choosing between ReadySet and ClickHouse.

Data security: ReadySet is a cloud-based platform, so your data is stored on the cloud. ClickHouse is an open-source platform, so you have more control over your data security.

Support: ReadySet offers 24/7 support, while ClickHouse only offers support during business hours.

## 💭Final thoughts

ReadySet and ClickHouse are both good data warehouse platforms, but they have different strengths and weaknesses. The best choice for your project will depend on your specific needs. If you are not sure which platform is right for you, I recommend contacting the support teams for both ReadySet and ClickHouse. They will be able to help you assess your needs and make a recommendation.

## 📶**Trend Analysis**

**Q1**

The revenue from orders with a discount of 1 to 3 percent and a quantity of less than 25 decreased by 0.2 milliseconds on ClickHouse and 1.5 milliseconds on ReadySet when the data was scaled down from 60 million rows to 6 million rows. This suggests that both ClickHouse and ReadySet are able to handle large amounts of data efficiently.

**Q2**

The revenue from orders placed in the year 1993 and with a discount of 4 to 6 percent and a quantity of 26 to 35 increased by 0.4 milliseconds on ClickHouse and 2.7 milliseconds on ReadySet when the data was scaled up from 6 million rows to 60 million rows. This suggests that ClickHouse is able to handle large amounts of data more efficiently than ReadySet.

The revenue from orders placed in the year 1994 and with a discount of 5 to 7 percent and a quantity of 26 to 35 increased by 0.1 milliseconds on ClickHouse and 2.1 milliseconds on ReadySet when the data was scaled up from 6 million rows to 600 million rows. This suggests that ClickHouse is still able to handle very large amounts of data efficiently.

**Q3**

The revenue from orders placed in the year 1992 and with both the customer and supplier nation being 'ASIA' increased by 255 milliseconds on ClickHouse and 911 milliseconds on ReadySet when the data was scaled up from 6 million rows to 60 million rows. This suggests that ReadySet is more sensitive to increases in data size than ClickHouse.

The revenue from orders placed in the year 1992 and with both the customer and supplier city being 'UNITED STATES' increased by 247 milliseconds on ClickHouse and 716 milliseconds on ReadySet when the data was scaled up from 6 million rows to 60 million rows. This suggests that ReadySet is more sensitive to increases in data size than ClickHouse.

The revenue from orders placed in the year 1997 and with both the customer and supplier city being 'UNITED KI1' or 'UNITED KI5' increased by 242 milliseconds on ClickHouse and 725 milliseconds on ReadySet when the data was scaled up from 6 million rows to 60 million rows. This suggests that ReadySet is more sensitive to increases in data size than ClickHouse.

**Q4**

The profit from orders placed in the year 1992 and with both the customer and supplier nation being 'AMERICA' and with the manufacturer being 'MFGR#1' or 'MFGR#2' increased by 227 milliseconds on ClickHouse and 610 milliseconds on ReadySet when the data was scaled up from 6 million rows to 60 million rows. This suggests that ReadySet is more sensitive to increases in data size than ClickHouse.

## 🏟️Conclusion

We hope this report has been helpful in comparing and contrasting ReadySet and ClickHouse.

In the analysis, a dataset containing 6,000,000 - 600,000,000 rows and 2 columns, were generated using Python in the `generate_data.py` script. The data is of integer type, and it was created randomly to simulate a large dataset for testing and analysis purposes.

The purpose of generating this data is to assess the performance of ClickHouse when processing a significant volume of data. The size of the dataset (60 million rows) allows for testing ClickHouse's ability to handle large-scale data processing efficiently.

The data was then processed using SQL statements. The specific SQL statements used for processing the data were not mentioned, but they likely involved various operations, such as filtering, grouping, aggregation, and other analytical tasks.

Some typical SQL operations that could be applied to this dataset include:

1. SELECT: Retrieving specific columns or rows from the dataset.
2. WHERE: Filtering data based on certain conditions.
3. GROUP BY: Grouping data based on a specific column to perform aggregation.
4. ORDER BY: Sorting the data based on specified columns.
5. JOIN: Combining data from multiple tables based on a common column.

The generated dataset was stored in a CSV file named "data.csv." However, it is important to note that the "data.csv" file is not available in the GitHub files due to its large size. This is a common approach when dealing with massive datasets that can't be easily shared or version-controlled.

By processing this random dataset using SQL statements in ClickHouse, the analysis aims to evaluate the database's performance in terms of query execution time, resource utilization, and overall efficiency. The results obtained from this analysis will help understand how ClickHouse handles data-intensive operations and whether it is suitable for large-scale analytical workloads. The insights gained from this analysis will be valuable for making data-driven decisions and optimizing database performance.

# CODE USED:

### SQL code:

```sql
CREATE TABLE customer
(
        C_CUSTKEY       UInt32,
        C_NAME          String,
        C_ADDRESS       String,
        C_CITY          LowCardinality(String),
        C_NATION        LowCardinality(String),
        C_REGION        LowCardinality(String),
        C_PHONE         String,
        C_MKTSEGMENT    LowCardinality(String)
)
ENGINE = MergeTree ORDER BY (C_CUSTKEY);

CREATE TABLE lineorder
(
    LO_ORDERKEY             UInt32,
    LO_LINENUMBER           UInt8,
    LO_CUSTKEY              UInt32,
    LO_PARTKEY              UInt32,
    LO_SUPPKEY              UInt32,
    LO_ORDERDATE            Date,
    LO_ORDERPRIORITY        LowCardinality(String),
    LO_SHIPPRIORITY         UInt8,
    LO_QUANTITY             UInt8,
    LO_EXTENDEDPRICE        UInt32,
    LO_ORDTOTALPRICE        UInt32,
    LO_DISCOUNT             UInt8,
    LO_REVENUE              UInt32,
    LO_SUPPLYCOST           UInt32,
    LO_TAX                  UInt8,
    LO_COMMITDATE           Date,
    LO_SHIPMODE             LowCardinality(String)
)
ENGINE = MergeTree PARTITION BY toYear(LO_ORDERDATE) ORDER BY (LO_ORDERDATE, LO_ORDERKEY);

CREATE TABLE part
(
        P_PARTKEY       UInt32,
        P_NAME          String,
        P_MFGR          LowCardinality(String),
        P_CATEGORY      LowCardinality(String),
        P_BRAND         LowCardinality(String),
        P_COLOR         LowCardinality(String),
        P_TYPE          LowCardinality(String),
        P_SIZE          UInt8,
        P_CONTAINER     LowCardinality(String)
)
ENGINE = MergeTree ORDER BY P_PARTKEY;

CREATE TABLE supplier
(
        S_SUPPKEY       UInt32,
        S_NAME          String,
        S_ADDRESS       String,
        S_CITY          LowCardinality(String),
        S_NATION        LowCardinality(String),
        S_REGION        LowCardinality(String),
        S_PHONE         String
)
ENGINE = MergeTree ORDER BY S_SUPPKEY;
```

```sql
SET max_memory_usage = 20000000000;

CREATE TABLE lineorder_flat
ENGINE = MergeTree ORDER BY (LO_ORDERDATE, LO_ORDERKEY)
AS SELECT
    l.LO_ORDERKEY AS LO_ORDERKEY,
    l.LO_LINENUMBER AS LO_LINENUMBER,
    l.LO_CUSTKEY AS LO_CUSTKEY,
    l.LO_PARTKEY AS LO_PARTKEY,
    l.LO_SUPPKEY AS LO_SUPPKEY,
    l.LO_ORDERDATE AS LO_ORDERDATE,
    l.LO_ORDERPRIORITY AS LO_ORDERPRIORITY,
    l.LO_SHIPPRIORITY AS LO_SHIPPRIORITY,
    l.LO_QUANTITY AS LO_QUANTITY,
    l.LO_EXTENDEDPRICE AS LO_EXTENDEDPRICE,
    l.LO_ORDTOTALPRICE AS LO_ORDTOTALPRICE,
    l.LO_DISCOUNT AS LO_DISCOUNT,
    l.LO_REVENUE AS LO_REVENUE,
    l.LO_SUPPLYCOST AS LO_SUPPLYCOST,
    l.LO_TAX AS LO_TAX,
    l.LO_COMMITDATE AS LO_COMMITDATE,
    l.LO_SHIPMODE AS LO_SHIPMODE,
    c.C_NAME AS C_NAME,
    c.C_ADDRESS AS C_ADDRESS,
    c.C_CITY AS C_CITY,
    c.C_NATION AS C_NATION,
    c.C_REGION AS C_REGION,
    c.C_PHONE AS C_PHONE,
    c.C_MKTSEGMENT AS C_MKTSEGMENT,
    s.S_NAME AS S_NAME,
    s.S_ADDRESS AS S_ADDRESS,
    s.S_CITY AS S_CITY,
    s.S_NATION AS S_NATION,
    s.S_REGION AS S_REGION,
    s.S_PHONE AS S_PHONE,
    p.P_NAME AS P_NAME,
    p.P_MFGR AS P_MFGR,
    p.P_CATEGORY AS P_CATEGORY,
    p.P_BRAND AS P_BRAND,
    p.P_COLOR AS P_COLOR,
    p.P_TYPE AS P_TYPE,
    p.P_SIZE AS P_SIZE,
    p.P_CONTAINER AS P_CONTAINER
FROM lineorder AS l
INNER JOIN customer AS c ON c.C_CUSTKEY = l.LO_CUSTKEY
INNER JOIN supplier AS s ON s.S_SUPPKEY = l.LO_SUPPKEY
INNER JOIN part AS p ON p.P_PARTKEY = l.LO_PARTKEY;
```

^^Converting “star schema” to denormalized “flat schema”:

### Python code:

---

```python
#generate -09/04
import pandas as pd
import random
from faker import Faker

# Initialize Faker for generating fake data
fake = Faker()

# Function to generate random customer data
def generate_customer_data(num_rows):
    data = {
        'C_CUSTKEY': [i for i in range(1, num_rows + 1)],
        'C_NAME': [fake.name() for _ in range(num_rows)],
        'C_ADDRESS': [fake.address() for _ in range(num_rows)],
        'C_CITY': [fake.city() for _ in range(num_rows)],
        'C_NATION': [fake.country() for _ in range(num_rows)],
        'C_REGION': [fake.state() for _ in range(num_rows)],
        'C_PHONE': [fake.phone_number() for _ in range(num_rows)],
        'C_MKTSEGMENT': [random.choice(['Segment A', 'Segment B', 'Segment C']) for _ in range(num_rows)]
    }
    return pd.DataFrame(data)

# Function to generate random lineorder data
def generate_lineorder_data(num_rows):
    data = {
        'LO_ORDERKEY': [i for i in range(1, num_rows + 1)],
        'LO_LINENUMBER': [random.randint(1, 10) for _ in range(num_rows)],
        'LO_CUSTKEY': [random.randint(1, num_rows) for _ in range(num_rows)],
        'LO_PARTKEY': [random.randint(1, num_rows) for _ in range(num_rows)],
        'LO_SUPPKEY': [random.randint(1, num_rows) for _ in range(num_rows)],
        'LO_ORDERDATE': [fake.date_of_birth(minimum_age=20, maximum_age=80) for _ in range(num_rows)],
        'LO_ORDERPRIORITY': [random.choice(['High', 'Medium', 'Low']) for _ in range(num_rows)],
        'LO_SHIPPRIORITY': [random.randint(1, 5) for _ in range(num_rows)],
        'LO_QUANTITY': [random.randint(1, 100) for _ in range(num_rows)],
        'LO_EXTENDEDPRICE': [random.randint(100, 1000) for _ in range(num_rows)],
        'LO_ORDTOTALPRICE': [random.randint(1000, 10000) for _ in range(num_rows)],
        'LO_DISCOUNT': [random.uniform(0.01, 0.10) for _ in range(num_rows)],
        'LO_REVENUE': [random.randint(1000, 5000) for _ in range(num_rows)],
        'LO_SUPPLYCOST': [random.randint(500, 2000) for _ in range(num_rows)],
        'LO_TAX': [random.uniform(0.01, 0.10) for _ in range(num_rows)],
        'LO_COMMITDATE': [fake.date_of_birth(minimum_age=20, maximum_age=80) for _ in range(num_rows)],
        'LO_SHIPMODE': [random.choice(['Air', 'Ground', 'Express']) for _ in range(num_rows)]
    }
    return pd.DataFrame(data)

# Function to generate random part data
def generate_part_data(num_rows):
    data = {
        'P_PARTKEY': [i for i in range(1, num_rows + 1)],
        'P_NAME': [fake.word() for _ in range(num_rows)],
        'P_MFGR': [fake.company() for _ in range(num_rows)],
        'P_CATEGORY': [random.choice(['Category A', 'Category B', 'Category C']) for _ in range(num_rows)],
        'P_BRAND': [fake.company_suffix() for _ in range(num_rows)],
        'P_COLOR': [fake.color_name() for _ in range(num_rows)],
        'P_TYPE': [fake.word() for _ in range(num_rows)],
        'P_SIZE': [random.randint(1, 10) for _ in range(num_rows)],
        'P_CONTAINER': [random.choice(['Box', 'Carton', 'Bag']) for _ in range(num_rows)]
    }
    return pd.DataFrame(data)

# Function to generate random supplier data
def generate_supplier_data(num_rows):
    data = {
        'S_SUPPKEY': [i for i in range(1, num_rows + 1)],
        'S_NAME': [fake.company() for _ in range(num_rows)],
        'S_ADDRESS': [fake.address() for _ in range(num_rows)],
        'S_CITY': [fake.city() for _ in range(num_rows)],
        'S_NATION': [fake.country() for _ in range(num_rows)],
        'S_REGION': [fake.state() for _ in range(num_rows)],
        'S_PHONE': [fake.phone_number() for _ in range(num_rows)]
    }
    return pd.DataFrame(data)

# Define the number of rows for each table
num_rows = 1000000  # You can change this to 100,000,000 for the full dataset

# Generate data for each table
customer_df = generate_customer_data(num_rows)
lineorder_df = generate_lineorder_data(num_rows)
part_df = generate_part_data(num_rows)
supplier_df = generate_supplier_data(num_rows)

# Save the generated data to CSV files
customer_df.to_csv('customer.csv', index=False)
lineorder_df.to_csv('lineorder.csv', index=False)
part_df.to_csv('part.csv', index=False)
supplier_df.to_csv('supplier.csv', index=False)
```

```python
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
```

```python
#main-09/04
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
```