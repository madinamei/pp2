import psycopg2
from config import load_config

def create_tables():
    conn = psycopg2.connect(**load_config())
    cur = conn.cursor()

    # groups
    cur.execute("""
        CREATE TABLE IF NOT EXISTS groups (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50) UNIQUE NOT NULL
        );
    """)

    # contacts
    cur.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(100),
            birthday DATE,
            group_id INTEGER REFERENCES groups(id)
        );
    """)

    # phones
    cur.execute("""
        CREATE TABLE IF NOT EXISTS phones (
            id SERIAL PRIMARY KEY,
            contact_id INTEGER REFERENCES contacts(id) ON DELETE CASCADE,
            phone VARCHAR(20) NOT NULL,
            type VARCHAR(10) CHECK (type IN ('home','work','mobile'))
        );
    """)

    conn.commit()
    cur.close()
    conn.close()

    print("Tables created successfully!")

create_tables()