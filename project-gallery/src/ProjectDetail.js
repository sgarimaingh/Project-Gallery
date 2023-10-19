import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import './ProjectDetail.css';

const ProjectDetail = () => {
  const { projectId } = useParams();
  const [project, setProject] = useState({});

  useEffect(() => {
    const fetchProject = async () => {
      const response = await fetch(`http://localhost:5000/projects/${projectId}`);
      const data = await response.json();
      setProject(data);
    };
    fetchProject();
  }, [projectId]);

  

  return (
    <div>
        {console.log(project.title)}
      <div className="project-detail">
        <h2>{project.title}</h2>
        <p>Project Technologies: {project.technologies}</p>
        <p>Frontend: {project.frontend}</p>
        <p>Backend: {project.backend}</p>
        <p>Databases: {project.databases}</p>
        <p>Infrastructure: {project.infrastructure}</p>
        <p>Availability: {project.availability}</p>
      </div>
    </div>
  );
};

export default ProjectDetail;

