import psycopg2

if __name__ == "__main__" :

    conn_details = psycopg2.connect(
        host="localhost",
        database="piscineds",
        user="jfrancis",
        password="mysecretpassword",
        port= '5432'
    )

    if conn_details:
        print("Connected to base")
    cursor = conn_details.cursor()
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
