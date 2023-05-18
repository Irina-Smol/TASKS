import pandas as pd
import psycopg2

from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

def create_table_from_csv(file_path, db_name, table_name, user, password, host='localhost'):
    # Load the CSV in pandas dataframe
    df = pd.read_csv(file_path)

    # Create a connection to the database
    conn = psycopg2.connect(
        dbname=db_name,
        user=user,
        password=password,
        host=host
    )
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = conn.cursor()

    # Drop the table if it already exists
    cursor.execute(sql.SQL("DROP TABLE IF EXISTS {}").format(sql.Identifier(table_name)))

    # Create the table
    create_table_query = 'CREATE TABLE {} ('.format(table_name) + ', '.join(['{} {}'.format(field, 'TEXT' if df[field].dtype == 'object' else 'NUMERIC') for field in df.columns]) + ')'
    cursor.execute(create_table_query)

    # Insert data into the table
    for index, row in df.iterrows():
        insert_query = 'INSERT INTO {} VALUES ('.format(table_name) + ', '.join(['%s' for _ in range(len(row))]) + ')'

        cursor.execute(insert_query, tuple(row))

    # Close the connection
    conn.close()

create_table_from_csv('path_to_your_file.csv', 'your_database_name', 'your_table_name', 'your_username', 'your_password')
