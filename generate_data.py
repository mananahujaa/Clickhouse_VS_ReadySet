#generate -09/05
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
