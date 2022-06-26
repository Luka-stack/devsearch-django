const projectsURL = 'http://localhost:8000/api/projects/';
const domain = 'http://localhost:8000';

let loginBtn = document.getElementById('login-btn');
let logoutBtn = document.getElementById('logout-btn');

let token = localStorage.getItem('token');

if (token) {
  loginBtn.remove();
} else {
  logoutBtn.remove();
}

logoutBtn.addEventListener('click', (event) => {
  event.preventDefault();
  localStorage.removeItem('token');
  window.location = 'http://127.0.0.1:5500/client/login.html';
});

const getProjects = () => {
  fetch(projectsURL)
    .then((response) => response.json())
    .then((data) => {
      buildProjects(data);
    });
};

const buildProjects = (data) => {
  const projectSection = document.getElementById('projects--wrapper');

  for (let i = 0; i < data.length; i++) {
    let project = data[i];

    let projectCard = `
        <div class="project--card">
            <img src="${domain}${project.featured_image}" />
            
            <div>
                <div class="card--header">
                    <h3>${project.title}</h3>
                    <strong class="vote--option" data-vote="up" data-project="${
                      project.id
                    }" >➕</strong>
                    <strong class="vote--option" data-vote="down" data-project="${
                      project.id
                    }" >➖</strong>
                </div>
                <i>${project.vote_ratio}% Positive Feedback</i>
                <p>${project.description.substring(0, 150)}</p>
            </div>

        </div>
    `;

    projectSection.innerHTML += projectCard;
  }

  // Add an Listener
  addVoteEvents();
};

const addVoteEvents = () => {
  const voteBtns = document.getElementsByClassName('vote--option');

  for (let i = 0; voteBtns.length > i; ++i) {
    voteBtns[i].addEventListener('click', (event) => {
      let vote = event.target.dataset.vote;
      let projectId = event.target.dataset.project;

      fetch(`${domain}/api/projects/${projectId}/vote/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify({
          value: vote,
        }),
      })
        .then((response) => response.json())
        .then((data) => console.log('Success:', data));
    });
  }
};

getProjects();
