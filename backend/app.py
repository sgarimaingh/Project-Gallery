from typing import Optional
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from database import create_database
from list_projects import list_projects
from get_project_by_id import get_project_by_id

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

create_database()

# API to retrieve all projects
@app.get('/projects')
def get_projects(query: Optional[str] = None):
    return list_projects(query)
    
    
# API to retrieve a project by ID
@app.get('/projects/{project_id}')
def get_project(project_id: int):
    return get_project_by_id(project_id)
    
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)

