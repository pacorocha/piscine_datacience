import os
import psycopg2
import time
from dotenv import load_dotenv

if __name__ == "__main__" :

    load_dotenv()
    max_retries = 10
    retry_delay = 2

    for attempt in range(max_retries):
        try:
            conn_details = psycopg2.connect(
                host="localhost",
                database=os.getenv("POSTGRES_DB"),
                user=os.getenv("POSTGRES_USER"),
                password=os.getenv("POSTGRES_PASSWORD"),
                port= '5432'
            )
            break
        except psycopg2.OperationalError:
            if attempt < max_retries - 1:
                print(f"Connection attempt {attempt + 1} failed. Retrying in {retry_delay} seconds...")
                time.sleep(retry_delay)
            else:
                print("Failed to connect to database after all retries")
                raise

    if conn_details:
        print("Connected to base")
    cursor = conn_details.cursor()

    create_enum_type = '''
        DO $$ BEGIN
            CREATE TYPE event_type AS ENUM ('view', 'cart', 'purchase', 'remove_from_cart');
        EXCEPTION
            WHEN duplicate_object THEN null;
        END $$;
    '''

    table_creation = '''
        CREATE TABLE IF NOT EXISTS public.data_2022_oct
        (
            event_time time with time zone,
            event_type event_type,
            product_id integer,
            price money,
            user_id bigint,
            user_session uuid
        )

        TABLESPACE pg_default;

        ALTER TABLE IF EXISTS public.data_2022_oct
            OWNER to jfrancis;
        '''
    cursor.execute(create_enum_type)
    cursor.execute(table_creation)
    conn_details.commit()
    cursor.close()
    conn_details.close()

def palindromeIndex(s):
    if s == s[::-1]:
        return -1
    result_s = ""
    for i in range(len(s)):
        for j in range(len(s)):
            if s[i] != s[j]:
                result_s += s[j]
            if result_s == result_s[::-1]:
                return j
