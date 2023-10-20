from database import connect_database
from fastapi.encoders import jsonable_encoder
from typing import Optional


def list_projects(query: Optional[str] = None):
    cur = connect_database()
    cur.execute('SELECT * FROM projects')
    rows = cur.fetchall()
    projects = [dict(row) for row in rows]
    if query:
        query = query.lower()
        filtered_projects = [project for project in projects if
                             (project.get('backend') and query in project['backend'].lower()) or
                             (project.get('frontend') and query in project['frontend'].lower()) or
                             (project.get('databases') and query in project['databases'].lower()) or
                             (project.get('infrastructure') and query in project['infrastructure'].lower())]

        return jsonable_encoder(filtered_projects)
    else:
        return jsonable_encoder(projects)
