import psycopg2
connUrl="dbname='political_arena' host='localhost' port='5432' user='kamaa' password='DAka31..'"
def connection():
    try:
        connection= psycopg2.connect(connUrl)
        print(connection)
    except :
        print("conn lost")
    return connection

def CreateTable():
    conn=connection()
    cur=conn.cursor()
    create=tables()
    for creating_table in create:
        cur.execute(creating_table)
        conn.commit()
    
    
def tables():
    users_table = """CREATE TABLE IF NOT EXISTS users_table (
        id serial PRIMARY KEY NOT NULL,
        firstname character varying(50) NOT NULL,
        lastname character varying(50) NOT NULL,
        othernames character varying(50),
        username character varying(50) NOT NULL,
        email character varying(50),
        phonenumber character varying(30),
        password character varying(50) NOT NULL,
        passportUrl character varying(50),
        registered timestamp with time zone DEFAULT ('now'::text)::date NOT NULL,
        isAdmin boolean NOT NULL
    )"""

    party = """CREATE TABLE IF NOT EXISTS party_table (
        id serial PRIMARY KEY NOT NULL,
        name character varying(20) NOT NULL,
        hqAddress character varying(30) NOT NULL,
        logoUrl character varying(50)
        
    )"""
    office = """CREATE TABLE IF NOT EXISTS office_table (
        id serial PRIMARY KEY NOT NULL,
        name character varying(20) NOT NULL,
        type character varying(30) NOT NULL
        
    )"""

    queries = [users_table, party]
    return queries

    

