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
    return "created"
    
    
def tables():
    user= """CREATE TABLE IF NOT EXISTS user_table (
        id SERIAL PRIMARY KEY NOT NULL,
        firstname character varying(50) NOT NULL,
        lastname character varying(50) NOT NULL,
        othernames character varying(50),
        username character varying(50) NOT NULL UNIQUE,
        email character varying(50),
        phonenumber character varying(30),
        password character varying(100) NOT NULL,
        passportUrl character varying(50),
        isAdmin boolean NOT NULL
    )"""

    party = """CREATE TABLE IF NOT EXISTS party(
        id SERIAL PRIMARY KEY NOT NULL,
        name character varying(20) NOT NULL UNIQUE,
        hqAddress character varying(30) NOT NULL,
        logoUrl character varying(50) NOT NULL UNIQUE
        
    )"""
    office = """CREATE TABLE IF NOT EXISTS office (
        id SERIAL PRIMARY KEY NOT NULL,
        name character varying(20) NOT NULL UNIQUE,
        type character varying(30) NOT NULL
        
    )"""

    candidate = """CREATE TABLE IF NOT EXISTS candidate(
        id SERIAL PRIMARY KEY NOT NULL,
        office_id INT NOT NULL REFERENCES office(id) ON DELETE CASCADE,
        party_id INT NOT NULL REFERENCES party(id) ON DELETE CASCADE,
        candidate_id INT NOT NULL REFERENCES user_table(id) ON DELETE CASCADE,
        UNIQUE(party_id,candidate_id)
    
    )"""

    vote = """CREATE TABLE IF NOT EXISTS vote (
        id SERIAL PRIMARY KEY NOT NULL,
        createdOn timestamp with time zone DEFAULT ('now'::text)::date NOT NULL,
        createdBy INT NOT NULL REFERENCES user_table(id) ON DELETE CASCADE,
        office_id INT NOT NULL REFERENCES office(id) ON DELETE CASCADE,
        candidate_id INT NOT NULL REFERENCES candidate(id) ON DELETE CASCADE,
        UNIQUE(createdBy,office_id,candidate_id)
        
    )"""
    petition = """CREATE TABLE IF NOT EXISTS petition(
        id SERIAL PRIMARY KEY NOT NULL,
        createdOn timestamp with time zone DEFAULT ('now'::text)::date NOT NULL,
        createdBy INT NOT NULL REFERENCES user_table(id) ON DELETE CASCADE,
        office_id INT NOT NULL REFERENCES office(id) ON DELETE CASCADE,
        body character varying(20) NOT NULL,
        UNIQUE(createdBy,office_id)

    )"""




    queries = [user, party,office,candidate,vote,petition]
    print("tables created")
    return queries

    

