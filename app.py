from flask import Flask, jsonify
from flask_cors import CORS
import sqlite3
import pandas as pd

app = Flask(__name__)
CORS(app)

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

# API to retrieve all projects
@app.route('/projects', methods=['GET'])
def get_projects():
    conn = sqlite3.connect('projects.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute('SELECT * FROM projects')
    rows = cur.fetchall()
    conn.close()
    return jsonify([dict(row) for row in rows])

# API to retrieve a project by ID
@app.route('/projects/<int:project_id>', methods=['GET'])
def get_project(project_id):
    conn = sqlite3.connect('projects.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute('SELECT * FROM projects WHERE id = ?', (project_id,))
    row = cur.fetchone()
    conn.close()
    if row:
        return jsonify(dict(row))
    else:
        return jsonify({'error': 'Project not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
