import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import './ProjectDetail.css';

const ProjectDetail = () => {
    const { projectId } = useParams();
    const [project, setProject] = useState({}); // Set initial state to empty object
  
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
        <div className="project-details">
            <h2>{project.title}</h2><hr/>&nbsp;
              <p class="key"> Title  </p>
                <p class="value">{project.title}</p>
              <p class="key">Project.Technologies   </p>
                <p class="value">{project.technologies} </p>
              <p class="key">Technical_SkillSet.Frontend  </p>
                <p class="value">{project.frontend}</p>
              <p class="key">Technical_SkillSet.Backend  </p>
                <p class="value"> {project.backend}</p>
              <p class="key">Technical_SkillSet.Databases  </p>
                <p class="value">{project.databases ? project.databases : '—-'} </p>
              <p class="key"> Technical_SkillSet.Infrastructure  </p>
                <p class="value">{project.infrastructure ? project.infrastructure : '—-'}</p>
        </div>
      </div>
    );
  };

export default ProjectDetail;

