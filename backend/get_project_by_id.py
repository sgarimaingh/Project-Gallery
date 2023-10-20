from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from database import connect_database
from fastapi.encoders import jsonable_encoder

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_project_by_id(project_id: int):
    cur = connect_database()
    cur.execute('SELECT * FROM projects WHERE id = ?', (project_id,))
    row = cur.fetchone()
    if row:
        return jsonable_encoder(dict(row))
    else:
        response = {'error': 'Project not found'}
        return Response(content=response, status_code=404, media_type="application/json")
