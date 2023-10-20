import sqlite3
import pandas as pd


def create_database():
    # Load data into the database
    data = pd.read_excel('Parsed_FE Interviews_Cleaned.xlsx')

    # Create a SQLite database
    conn = sqlite3.connect('projects.db')
    cur = conn.cursor()

    cur.execute('DROP TABLE IF EXISTS projects')


    # Create a table
    cur.execute('''
        CREATE TABLE projects (
            id INTEGER PRIMARY KEY,
            title TEXT,
            technologies TEXT,
            frontend TEXT,
            backend TEXT,
            databases TEXT,
            infrastructure TEXT,
            availability TEXT
        )
    ''')

    # Insert data into the table
    for idx, item in data.iterrows():
        cur.execute('''
            INSERT INTO projects (id, title, technologies, frontend, backend, databases, infrastructure, availability) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (idx + 1, item['Project.Title'], item['Project.Technologies'], item['Technical_Skillset.Frontend'], item['Technical_Skillset.Backend'], item['Technical_Skillset.Databases'], item['Technical_Skillset.Infrastructre'], item['Other_Information.Availability']))


    conn.commit()
    conn.close()
    
def connect_database():
    conn = sqlite3.connect('projects.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    return cur
        
