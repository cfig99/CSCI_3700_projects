import psycopg2

# Connects to database
def connect_db():
    try:
        conn = psycopg2.connect(
            dbname="dvdrental",
            user="raywu1990",
            password="test",
            host="127.0.0.1",
            port="5432"
        )
        return conn
    except Exception as e:
        return str(e)


