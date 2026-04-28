import psycopg2
from config import load_config

def get_connection():
    conn = psycopg2.connect(**load_config())
    return conn