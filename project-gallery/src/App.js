import React, { useEffect, useState } from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import './App.css';
import ProjectDetail from './ProjectDetail';


function App() {
  const [projects, setProjects] = useState([]);
  const [searchTerm, setSearchTerm] = useState('');
  const [filteredProjects, setFilteredProjects] = useState([]);

  const handleSearch = async () => {
    if (searchTerm) {
      const response = await fetch(`http://localhost:5000/projects?query=${searchTerm}`);
      const data = await response.json();
      setFilteredProjects(data);
    } else {
      setFilteredProjects(projects);
    }
  };

  useEffect(() => {
    fetchProjects();
  }, []);

  const fetchProjects = async () => {
    const response = await fetch('http://localhost:5000/projects');
    const data = await response.json();
    setProjects(data);
    setFilteredProjects(data);
  };

  return (
    <Router>
      <div className="App">
        <h1>Project Gallery</h1>
        <input
          type="text"
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
          placeholder="Search projects by technical skill sets.."
          className='search-bar'
        />
        <button onClick={handleSearch} className='search-button'>Search</button>
        <div className="gallery">
          {filteredProjects.map((project) => (
            <Link
              key={project.id}
              to={`/project/${project.id}`}
              className="project-card"
            >
              <p><strong>Title</strong></p>
              <p>{project.title}</p>
              <p>
                <strong>Project.Technologies</strong> </p>
                <p>{project.technologies}
              </p>
              <p>
                <strong>Technical_SkillSet.Frontend</strong></p>
                <p>{project.frontend}
              </p>
              <p>
                <strong>Technical_SkillSet.Backend</strong></p>
                <p> {project.backend}
              </p>
              <p>
                <strong>Technical_SkillSet.Databases</strong></p>
                <p>
                {project.databases ? project.databases : '—-'}
              </p>
              <p>
                <strong>Technical_SkillSet.Infrastructure</strong></p>
                <p>{project.infrastructure ? project.infrastructure : '—-'}
              </p>
            </Link>
          ))}
        </div>
        <Routes>
          <Route
            path="/project/:projectId"
            element={<ProjectDetail />}
          />
        </Routes>
      </div>
    </Router>
  );
}

export default App;